from flask import render_template,url_for,flash,redirect
from .forms import SignUpForm,LoginForm
from . import main


@main.route('/')
def home():

  return render_template('index.html')


@main.route('/signup', methods=['GET','POST'])
def signup():

  form = SignUpForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!','success')
    return redirect(url_for('home'))

  return render_template('signup.html', title='SIGN UP', form=form)


@main.route('/login',methods=['GET','POST'])
def login():

  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com and form.password.data' == 'password':
      flash('you have been loged in successfully','success')
      return redirect(url_for('home'))
    else:
      flash('login unsuccessfull. aithe email or password dont match','danger')  
  return render_template('login.html', title='LOG IN', form=form)

