from flask_wtf import Form
from wtforms import StringField, PasswordField

from wtforms.validators import DataRequired, Length

class NewUserForm(Form):
  username = StringField('username', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired()])