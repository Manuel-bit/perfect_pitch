from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class SignUpForm(FlaskForm):
  username=StringField('username',validators=[DataRequired(),Length(min=2,max=20)])
  email=StringField('email',validators = [DataRequired(), Email()])
  password=PasswordField('Password',validators=[DataRequired()])
  confirm_password = PasswordField('Password',validators=[DataRequired(),EqualTo('password')])
  submit = SubmitField('Sign up')