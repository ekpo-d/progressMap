from flask_wtf import Form
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

	title = StringField(validators=[DataRequired()])
	course = StringField(validators=[DataRequired()])
	curriculum = StringField(validators=[DataRequired()])
	description = StringField(widget=TextArea(), validators=[DataRequired()])