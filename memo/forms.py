from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import required, Length, DataRequired, ValidationError
from memo.models import User
from werkzeug.security import check_password_hash

class RegisterForm(FlaskForm):
    username = StringField(label='username',
        validators=[required(),
        Length(min=2, max=30,message="Username should be between 2 and 30 character"),
        DataRequired()])

    password = StringField(label='password',
        validators=[required(),
        Length(min=6, max=18, message="Password should be between 6 and 18 characters"),
        DataRequired()])

    submit = SubmitField(label='submit')

    def validate_username(self, username_to_check):
        users = User.query.filter_by(username=username_to_check.data).first()
        if users:
            raise ValidationError("Username taken")


class LoginForm(FlaskForm):
    username = StringField(label='username',
        validators=[required(), DataRequired()])

    password = StringField(label='password',
        validators=[required(), DataRequired()])

    submit = SubmitField(label='submit')

    def validate_username(self, username_to_check):
        users = User.query.filter_by(username=username_to_check.data).first()
        if not users:
            raise ValidationError("Username not registered")

    def validate_password(self, password_to_check):
        users = User.query.filter_by(username=self.username.data).first()
        if not users:
            return 

        password = User.query.filter_by(username=self.username.data).first().password
        if not check_password_hash(password, password_to_check.data):
            raise ValidationError("Wrong Password")