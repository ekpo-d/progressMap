from flask_wtf import Form
from wtforms.fields import StringField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class addForm(Form):
	title = StringField(validators=[DataRequired()])
	curriculum = StringField(validators=[DataRequired()])
	description = StringField(widget=TextArea(), validators=[DataRequired()])