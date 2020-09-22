from flask_wtf import FlaskForm
from wtforms import stringfield, PasswordField
from wtforms.validators import Input_required, Length, EqualTo


class  RegistrartionForm(FlaskForm):
    """ Registration form """

    username = stringfield ('username_label')
    password = PasswordField('password_label')
    confirm_pswd = PasswordField ('confirm_pswd_label')
