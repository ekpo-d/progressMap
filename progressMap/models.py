from sqlalchemy import desc
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from progressMap import db

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(40), unique = True)
	email = db.Column(db.String(120), unique = True)
	password_hash = db.Column(db.String)
	articles =  db.relationship('Articles', backref='user', lazy='dynamic')
	courses =  db.relationship('Courses', backref='user', lazy='dynamic')
	curriculums =  db.relationship('Curriculums', backref='user', lazy='dynamic')
	completed = db.relationship('Completed', backref='user', lazy='dynamic')
	allContent = db.relationship('AllContent', backref='user', lazy='dynamic')
	
	@property
	def password(self):
		raise AttributeError('password: write-only field')
		
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
		
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	
	@staticmethod
	def get_by_username(username):
		return User.query.filter_by(username=username).first()
	
	def __repr__(self):
		return '<User %s>' %self.username
	
class Articles(db.Model):
	id  = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(300), nullable=False)
	course = db.Column(db.Text, nullable=False)
	curriculum = db.Column(db.Text, nullable=False)
	description = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return "<Article '%s'>".format(self.title)
	
class Courses(db.Model):
	id  = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(300), nullable=False)
	curriculum = db.Column(db.Text, nullable=False)
	description = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return "<Course '%s'>".format(self.title)	
	
class Curriculums(db.Model):
	id  = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(300), nullable=False)
	description = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return "<Curriculums '%s'>".format(self.title)
	
class Completed(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(300), nullable=False)
	description = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return "<Completed '%s'>".format(self.title)
	
class AllContent(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(300), nullable=False)
	description = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return "<All user articles '%s'>".format(self.title)
	
def getFromDb(className, num):
	return className.query.order_by(desc(className.title)).limit(num)