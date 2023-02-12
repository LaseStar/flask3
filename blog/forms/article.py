from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField, SubmitField, SelectMultipleField


class CreateArticleForm(FlaskForm):
    title = StringField(
        "Title",
        [validators.DataRequired()],
    )
    body = TextAreaField(
        "Body",
        [validators.DataRequired()],
    )
    submit = SubmitField("Publish")
    tags = SelectMultipleField("Tags", coerce=int)
