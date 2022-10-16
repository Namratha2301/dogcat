import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    ENVIRONMENT = os.environ.get('environment')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sjskfdojg&*&(9')

class development(Config):
    DEBUG = True

class production(Config):
    DEBUG = False
