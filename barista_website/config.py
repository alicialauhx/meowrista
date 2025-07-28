import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    ''' Configuration settings are defined inside the Config class. 
        Configuration file to store all configuration variables. 
        This can then be loaded when the app runs.
    '''

    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False

    # SECRET_KEY variable's value is used as a cryptographic key
    # Set with two terms joined by the 'or' operator.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # The extension takes the location of the application's databse from the 
    # SQLALCHEMY_DATABASE_URI configuration variable
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    

    # Set to false to disable a feature of Flask-SQLAlchemy that we don't need
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    FLASK_ENV = 'production'

class DevelopmentConfig(Config):
    DEBUG = True