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
        validators.Length(min=5, max=50)])

    user_id = IntegerField("User Id", [validators.NumberRange(1, 99999)])
    balance = IntegerField("Balance", [validators.NumberRange(1, 99999)])
    total = IntegerField("Amount", [validators.NumberRange(-999999, 999999)])
    created_on = DateField("Date")

    submit = SubmitField()


class TransactionForm(FlaskForm):
    transaction_number = StringField('Account No', [
        validators.DataRequired(),
        validators.Length(min=5,max=20)

    ], description="You need to enter transaction number")
    account = IntegerField('account')
    amount = FloatField('amount')
    name = StringField('Name', [
        validators.DataRequired(),
        validators.Length(min=5, max=50)

    ], description="You need to enter account number")
    date=DateField('Date')
    type=StringField('Transaction Type')
    submit = SubmitField()

