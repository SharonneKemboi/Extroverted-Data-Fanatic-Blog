from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField,ValidationError,BooleanField
from wtforms.validators import DataRequired, EqualTo, Email
from app.models import User


#first class
class RegistrationForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("pass_confirm", message="Passwords do not match")])
    pass_confirm = PasswordField("Confirm password", validators = [DataRequired()])
    submit = SubmitField("Register")

    def validate_username(self,data_field):
        if User.query.filter_by(name = data_field.data).first():
            raise ValidationError("username is already exists")


    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("This account already exists")   


#second class
class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")            