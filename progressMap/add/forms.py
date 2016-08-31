from flask_wtf import Form
from wtforms.fields import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, ValidationError

class articleForm(Form):
	title = StringField(validators=[DataRequired()])
	course = StringField(validators=[DataRequired()])
	curriculum = StringField(validators=[DataRequired()])
	description = StringField(widget=TextArea(), validators=[DataRequired()])
	
class courseForm(Form):
	title = StringField(validators=[DataRequired()])
	curriculum = StringField(validators=[DataRequired()])
	description = StringField(widget=TextArea(), validators=[DataRequired()])
	
class curriculumForm(Form):
	title = StringField(validators=[DataRequired()])
	description = StringField(widget=TextArea(), validators=[DataRequired()])