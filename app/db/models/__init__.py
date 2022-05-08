from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash
from app.db import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False, unique=True)
    about = db.Column(db.String(300), nullable=True, unique=False)
    authenticated = db.Column(db.Boolean, default=False)
    registered_on = db.Column('registered_on', db.DateTime)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    is_admin = db.Column('is_admin', db.Boolean(), nullable=False, server_default='0')

    # `roles` and `groups` are reserved words that *must* be defined
    # on the `User` model to use group- or role-based authorization.

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.email



class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    balance = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    created_on = db.Column('created_on', db.DateTime)
    active = db.Column('is_active', db.Boolean(), nullable=False)
    #id balance total
    def __init__(self, account_number, name):
        self.account_number = account_number
        self.name = name
        self.balance = 0


    def is_active(self):
        return True


    def get_accout_number(self):
        return self.account_number


    def __repr__(self):
        return f"self.account_number"

class Transactions(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    transaction_number = db.Column(db.Integer, nullable=False, unique=True)
    account = db.Column(db.Integer, db.ForeignKey('account.id'))
    amount = db.Column(db.Float, nullable=False)
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return f"self.amount"
