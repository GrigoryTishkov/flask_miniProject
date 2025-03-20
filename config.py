import uuid
#from app import app
import os
basedir = os.path.abspath(os.path.dirname(__file__))
#uuid.uuid4().hex
SEC_HEX_KEY = "81b99e2d1d904a7db404a2e03b991b72"
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or SEC_HEX_KEY
    CSRF_ENABLED = True
   # app.config["SECRET_KEY"] = SEC_HEX_KEY
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')