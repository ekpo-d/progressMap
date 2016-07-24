from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
	username = StringField(validators=[DataRequired()])
	password = PasswordField(validators=[DataRequired()])
	remember_me = BooleanField('Remember me')
	
class SignupForm(Form):
	username = StringField(validators=[DataRequired()])
	email = StringField(validators=[DataRequired()])
	password = PasswordField(validators=[DataRequired()])
	ConfirmPassword = PasswordField(validators=[DataRequired()])
	remember_me = BooleanField('Remember me')
	