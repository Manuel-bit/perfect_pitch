from flask import render_template,url_for,flash,redirect
from .forms import LoginForm
from . import auth

@auth.route('/login',methods=['GET','POST'])
def login():

  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com and form.password.data' == 'password':
      flash('you have been loged in successfully','success')
      return redirect(url_for('home'))
    else:
      flash('login unsuccessfull. aithe email or password dont match','danger')  
  return render_template('login.html', title='LOG IN', form=form)

