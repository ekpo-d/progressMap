import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG=True
    SECRET_KEY='\xcbP\x08\xf1\x9c\xe8\x9fq\x19\xf7\xf9\xb4\x05\xe3\xbc\x98A\x04\x9fw\xfa\t\x1cN'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'models.db')

class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_RECORD_QUERIES = False

class DevelopmentConfig(Config):
    DEBUG_TB_INTERCEPT_REDIRECTS=False
