from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    # DataRequired() do not allow whitespaces in strings
    # Email() validate email adress
    username = StringField('Username', [
        validators.DataRequired(),
        validators.Length(min=4, max=25)
    ])
    email = StringField('Email', [
        validators.DataRequired(),
        validators.Length(min=6, max=35),
        validators.Email()
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=4, max=25)
    ])
    
    submit = BooleanField('Signup', [validators.DataRequired()])