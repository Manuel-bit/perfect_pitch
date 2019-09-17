from flask import render_template
from . import main
from . forms import SignUpForm
from flask_login import login_required

@main.route('/')
@login_required
def home():

  return render_template('index.html')

@main.route('/signup', methods=['GET','POST'])
def signup():

  form = SignUpForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!','success')
    return redirect(url_for('home'))

  return render_template('signup.html', title='SIGN UP', form=form)
