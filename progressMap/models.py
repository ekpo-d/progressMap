from datetime import datetime

from progressMap import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(40), unique = True)
	email = db.Column(db.String(120), unique = True)
	articles =  db.relationship('Articles', backref='user', lazy='dynamic')
	completed = db.relationship('Completed', backref='user', lazy='dynamic')
	allArticles = db.relationship('allCompleted', backref='user', dynamic='loading')
	
	def __repr__(self):
		return '<User %r>' %self.username
	
class Articles(db.Model):
	id  = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(300), nullable=False)
	description = db.Column(db.Text, nullable=False)
	date = db.Column(db.DateTime, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return "<Article '%r'>".format(self.title)
	
class Completed(db.Model):
	id = db.Column(db.Integer, primary_key = true)
	title = db.Column(db.String(300), nullable=False)
	description = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return "<Article '%r'>".format(self.title)