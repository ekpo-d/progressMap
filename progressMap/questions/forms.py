from flask_wtf import Form
from wtforms.fields import StringField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class askForm(Form):
	title = StringField(validators=[DataRequired()])
	message = StringField(widget=TextArea(), validators=[DataRequired()])