from progressMap import app, db
from progressMap.models import User, Curriculums, Courses, Articles, Completed, AllContent, Questions, Comments
from flask.ext.script import Manager, prompt_bool
from flask.ext.migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def initdb():
	db.create_all()
	db.session.add(User(username='david', password='test', email='a@b.c'))
	db.session.add(User(username='ekpo', password='test', email='b@c.d'))
	db.session.commit()
	print 'Database initialized' 
	
@manager.command
def dropdb():
	if prompt_bool('Clear out the database? '):
		db.drop_all()
		print 'Dropped the database'

if __name__ == '__main__':
	manager.run()
