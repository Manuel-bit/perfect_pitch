from flask_wtf import FlaskForm
from wtforms import stringfield,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class SignUpForm(FlaskForm):
  username = stringfield('username',
                        validators=[DataRequired(),Lenght(min=2,max=20)])
  email = stringfield('email',  
                        validators = [DataRequired(), Email()]
  password = PasswordField('Password',validators=[DataRequired()])
  confirm_password = PasswordField('Password',
                        validators=[DataRequired(),EqualTo('password')])
  submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
  email = stringfield('email',  
                        validators = [DataRequired(), Email()]
  password = PasswordField('Password',validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')



  


