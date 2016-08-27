from flask_wtf import Form
from wtforms.fields import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired
from .. import models


class askForm(Form):
    title = StringField(validators=[DataRequired()])
    article = StringField(validators=[DataRequired()])
    message = StringField(widget=TextArea(), validators=[DataRequired()])

    def save(self, user):
        title = self.title.data
        articleTitle = models.returnDbObject(
            models.Articles, self.article.data.lower())
        message = self.message.data
        status = False
        if articleTitle:
            row = models.Questions(
                title=title, article=articleTitle, message=message, user=user)
            models.dbCommit(row)
            status = True
        return status


class commentForm(Form):
    message = StringField(widget=TextArea(), validators=[DataRequired()])

    def save(self, question, user):
        message = self.message.data
        row = models.Comments(message=message, question=question, user=user)
        models.dbCommit(row)

        return models.getComments(question)
