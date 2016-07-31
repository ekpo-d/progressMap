from progressMap import app, db
from progressMap.models import User, Curriculums, Courses, Articles, Completed, AllContent, Questions, Comments
from flask.ext.script import Manager, prompt_bool
from flask.ext.migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def insertData():
	david = User(username='david', password='test', email='a@b.c')
	python = Curriculums(title='python', description='This is the python curriculum', user=david)
	oop = Courses(title='oop', curriculum=python, description='This is the oop course', user=david)
	article = Articles(title='abstract data types', course=oop, curriculum=python, description='this is the article on abstract data types', user=david)
	
	db.session.add()
	
	db.session.add(david)
	db.session.add(python)
	db.session.add(oop)
	db.session.add(article)
	db.session.commit()
	print 'Data inserted' 
	
@manager.command
def dropdb():
	if prompt_bool('Clear out the database? '):
		db.drop_all()
		print 'Dropped the database'

if __name__ == '__main__':
	manager.run()
