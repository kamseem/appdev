from wtforms import Form, StringField, PasswordField, SubmitField, BooleanField, validators


class Registration(Form):
    name = StringField('Student Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    username = StringField('Username', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = StringField('Student Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=8, max=30), validators.DataRequired(), validators.EqualTo('confirmpass', message='Passwords do not match')])
    confirmpass  = PasswordField('Confirm Password')
    submit = SubmitField("Register")


class Login(Form):
    username = StringField('Username', [validators.Length(min=1, max=150), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=8, max=30), validators.DataRequired()])
    remember = BooleanField('Remember Me', [validators.DataRequired()])
    submit = SubmitField('Login')
