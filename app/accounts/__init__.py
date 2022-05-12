import csv
import logging
import os
from flask import Blueprint, current_app, render_template, abort, redirect, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from jinja2 import TemplateNotFound
from app import auth
from app.auth.decorators import admin_required
from app.auth.forms import login_form, profile_form, register_form, security_form, user_edit_form
from app.db import db
from app.accounts.forms import AccountForm, TransactionForm
from app.db.models import Account, Transactions, User
from werkzeug.security import generate_password_hash

from app import config
from app.accounts.forms import csv_upload
from werkzeug.utils import secure_filename

import datetime

accounts = Blueprint('accounts', __name__,
                     template_folder='templates')


@accounts.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@accounts.route('/dashboard')
def dashboard():
    try:
        return render_template('dashboard.html')
    except TemplateNotFound:
        abort(404)


@accounts.route('/register', methods=['POST', 'GET'])
def register_account():
    # if current_user.is_authenticated:
    # return redirect(url_for('auth.dashboard'))
    form = AccountForm()
    if form.validate_on_submit():
        # user = User.query.filter_by(email=form.email.data).first()
        account_number = form.account_number.data
        name = form.name.data
        user_id = form.user_id.data
        balance = form.balance.data

        account = Account(account_number=account_number, name=name, user_id=user_id, created_on=datetime.date.today(),
                          balance=balance)
        db.session.add(account)
        db.session.commit()

        flash('Congratulations, you are now a registered user!', "success")
        return redirect(url_for('auth.login'), 302)
    else:

        return render_template('account_register.html', form=form)


@accounts.route('/add_transaction', methods=['POST', 'GET'])
def add_transaction():
    # if current_user.is_authenticated:
    # return redirect(url_for('auth.dashboard'))
    form = TransactionForm()
    if form.validate_on_submit():
        # user = User.query.filter_by(email=form.email.data).first()
        account = form.account.data
        amount = form.amount.data
        type = form.type.data

        transaction = Transactions(account=account, amount=amount, type=type)
        db.session.add(transaction)
        db.session.commit()

        flash('Transaction made successfully!')
        return redirect(url_for('accounts.dashboard'), 302)
    else:
        return render_template('add_transaction.html', form=form)


@accounts.route('/login', methods=['POST', 'GET'])
def login():
    form = login_form()
    if current_user.is_authenticated:
        return redirect(url_for('accounts.dashboard'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('accounts.login'))
        else:
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Welcome", 'success')
            return redirect(url_for('accounts.dashboard'))
    return render_template('login.html', form=form)


@accounts.route('/register_user', methods=['POST', 'GET'])
def register_user():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    form = register_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(email=form.email.data, password=generate_password_hash(form.password.data))
            db.session.add(user)
            db.session.commit()
            if user.id == 1:
                user.is_admin = 1
                db.session.add(user)
                db.session.commit()
            flash('Congratulations, you are now a registered user!', "success")
            return redirect(url_for('accounts.login'), 302)
        else:
            flash('Already Registered')
            return redirect(url_for('accounts.login'), 302)
    return render_template('register.html', form=form)


@accounts.route("/logout")
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('accounts.login'))


@accounts.route('/transactions')
@login_required
@admin_required
def browse_transactions():
    current_app.logger.info('Info level log')
    current_app.logger.warning('Warning level log')
    data = Transactions.query.all()
    titles = [('id', 'Transaction ID'), ('amount', 'Amount'), ('type', 'Type'), ('balance', 'Balance')]
    # retrieve_url = ('accounts.retrieve_transaction', [('transaction_id', ':id')])
    # edit_url = ('accounts.edit_transaction', [('transaction_id', ':id')])
    # add_url = url_for('accounts.add_transaction')
    # delete_url = ('accounts.delete_transaction', [('transaction_id', ':id')])
    return render_template('browse.html', titles=titles, data=data, Transactions=Transactions,
                           record_type="Transactions")


@accounts.route('/transactions/upload', methods=['POST', 'GET'])
@login_required
def transactions_upload():
    form = csv_upload()
    if form.validate_on_submit():
        log = logging.getLogger("myApp")

        filename = secure_filename(form.file.data.filename)
        print(current_app.config.get('UPLOAD_FOLDER'))
        filepath = os.path.join(config.Config.UPLOAD_FOLDER, filename)
        print(filepath)

        form.file.data.save(filepath)
        # user = current_user
        # trans=Transactions.query.all()
        # for t in trans:
        #     db.session.delete(t)
        list_of_transactions = []
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            balance = 0

            for row in csv_file:
                balance+=float(row['AMOUNT'])
                transaction_entry = Transactions(float(row['AMOUNT']), row['TYPE'],balance)
                transaction_entry.update_balance()
                db.session.add(transaction_entry)

                db.session.commit()

        return redirect(url_for('accounts.browse_transactions'))

    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)


@accounts.route('/transactions/<int:transaction_id>')
@login_required
def retrieve_transaction(transaction_id):
    transaction = Transactions.query.get(transaction_id)
    return render_template('profile_view.html', transaction=transaction)
