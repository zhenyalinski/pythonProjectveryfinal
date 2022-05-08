from flask import Blueprint, render_template, abort, redirect, url_for, flash
from flask_login import current_user
from jinja2 import TemplateNotFound

from app import db
from app.accounts.forms import AccountForm
from app.db.models import Account

account = Blueprint('account', __name__,
                        template_folder='templates')


@account.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@account.route('/dashboard')
def dashboard():

    try:
        return render_template('dashboard.html')
    except TemplateNotFound:
        abort(404)



@account.route('/register', methods=['POST', 'GET'])
def register():
    #if current_user.is_authenticated:
        #return redirect(url_for('auth.dashboard'))
    form = AccountForm()
    if form.validate_on_submit():
        #user = User.query.filter_by(email=form.email.data).first()
        account_number = form.account_number.data
        name = form.name.data
        user_id=form.user_id.data
        balance=form.balance.data
        total=form.total.data
        created_on = form.created_on.data

        account = Account(account_number,name,user_id,balance,total,created_on)
        db.session.add(account)
        db.session.commit()

        flash('Congratulations, you are now a registered user!', "success")
        return redirect(url_for('auth.login'), 302)
    else:


        return render_template('account_register.html', form=form)




