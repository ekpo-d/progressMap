from flask_wtf import Form
from wtforms.fields import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, ValidationError
from .. import models


class articleForm(Form):
    title = StringField(validators=[DataRequired()])
    course = StringField(validators=[DataRequired()])
    curriculum = StringField(validators=[DataRequired()])
    description = StringField(widget=TextArea(), validators=[DataRequired()])

    def save(self, user):
        title = self.title.data.lower()
        course = models.returnDbObject(
            models.Courses, self.course.data.lower())
        curriculum = models.returnDbObject(
            models.Curriculums, self.curriculum.data.lower())
        description = self.description.data
        status = False
        if course and curriculum:
            row = models.Articles(title=title, course=course, curriculum=curriculum,
                                  description=description, user=user)
            models.dbCommit(row)
            status = True
        return status, title


class courseForm(Form):
    title = StringField(validators=[DataRequired()])
    curriculum = StringField(validators=[DataRequired()])
    description = StringField(widget=TextArea(), validators=[DataRequired()])

    def save(self, user):
        title = self.title.data.lower()
        description = self.description.data
        curriculum = models.returnDbObject(
            models.Curriculums, self.curriculum.data.lower())
        status = False
        if curriculum:
            row = models.Courses(
                title=title, curriculum=curriculum, description=description, user=user)
            models.dbCommit(row)
            status = True
        return status, title


class curriculumForm(Form):
    title = StringField(validators=[DataRequired()])
    description = StringField(widget=TextArea(), validators=[DataRequired()])

    def save(self, user):
        title = self.title.data.lower()
        description = self.description.data
        row = models.Curriculums(
            title=title, description=description, user=user)
        models.dbCommit(row)
        return self.title.data
