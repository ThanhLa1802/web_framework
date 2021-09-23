from logging import DEBUG
import os
SECRET_KEY  = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'sqlite:///store.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True