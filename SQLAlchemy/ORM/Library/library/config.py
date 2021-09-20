import os
SECRET_KEY  = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False