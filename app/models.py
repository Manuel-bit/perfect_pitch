from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
  __tablename__='users'
  id = db.Column(db.Integer,primary_key=True)
  username= db.Column(db.String(255))
  email= db.Column(db.String(255))
  pas_secure= db.Column(db.String(255))
  profile_pic= db.Column(db.String(100))
  pitches= db.relationship('Pitch',backref = 'user',lazy='dynamic')

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self,password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)



  def __repr__(self):
    return f'User {self.username}'

class Pitch(db.Model):
  __tablename__='pitches'
  id= db.Column(db.Integer, primary_key=True)
  pitch= db.Column(db.String(255))
  comment= db.Column(db.String(255))
  category=db.Column(db.String(255))
  downvote=db.Column(db.Integer)
  upvote= db.Column(db.Integer)
  user_id= db.Column(db.Integer,db.ForeignKey('users.id'))
  




