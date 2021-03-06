from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, TextAreaField
from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):
    # DataRequired() do not allow whitespaces in strings
    # Email() validate email adress
    username = StringField('Username', [
        validators.Length(min=4, max=25)
    ])
    email = StringField('Email', [
        validators.Length(min=6, max=35),
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=4, max=25)
    ])
    
    submit = SubmitField('Signup')


class PostForm(FlaskForm):

    title = StringField('Title', [
        validators.Length(max=128)
    ])
    slug = StringField('Slug', [
        validators.Length(max=128)
    ])
    content = TextAreaField('Content')
    submit = SubmitField('Upload')
