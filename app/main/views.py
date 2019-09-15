from flask import render_template,url_for
from .forms import SignUpForm,LoginForm
from . import main


@main.route('/')
def home():

  return render_template('index.html')


@main.route('/signup')
def signup():

  form = SignUpForm()

  return render_template('signup.html', title='SIGN UP', form=form)


@main.route('/login')
def login():

  form = LoginForm()

  return render_template('login.html', title='LOG IN', form=form)

