from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *



class AccountForm(FlaskForm):
    account_number = StringField('Account No', [
        validators.DataRequired(),
        validators.Length(min=5,max=20)

    ], description="You need to enter account number")

    name = StringField('Name', [
        validators.DataRequired(),
        validators.Length(min=5,max=20)

    ], description="You need to enter account number")
    
    user_id = IntegerField("User ID", [
        validators.DataRequired(),
        validators.NumberRange(1,100000)])   
   
    balance = FloatField("Balance", [
        validators.DataRequired(),
        validators.NumberRange(1,100000)])   
   
       

    submit = SubmitField()


class TransactionForm(FlaskForm):
    transaction_number = StringField('Transaction No', [
        validators.DataRequired(),
        validators.Length(min=5,max=20)

    ], description="You need to enter transaction number")
    account = IntegerField('Account')
    amount = FloatField('Amount')
    
    type=StringField('Transaction Type')
    submit = SubmitField()



class csv_upload(FlaskForm):
    file = FileField()
    submit = SubmitField()


class login_form(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),
    ])

    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.length(min=6, max=35)
    ])
    submit = SubmitField()


class register_form(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),

    ], description="You need to signup with an email")

    password = PasswordField('Create Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),

    ], description="Create a password ")
    confirm = PasswordField('Repeat Password', description="Please retype your password to confirm it is correct")
    submit = SubmitField()


class profile_form(FlaskForm):
    about = TextAreaField('About', [validators.length(min=6, max=300)],
                          description="Please add information about yourself")

    submit = SubmitField()

class user_edit_form(FlaskForm):
    about = TextAreaField('About', [validators.length(min=6, max=300)],
                          description="Please add information about yourself")
    is_admin = BooleanField('Admin', render_kw={'value':'1'})
    submit = SubmitField()


class security_form(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),

    ], description="You can change your email address")

    password = PasswordField('Create Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),

    ], description="Create a password ")
    confirm = PasswordField('Repeat Password', description="Please retype your password to confirm it is correct")

    submit = SubmitField()
