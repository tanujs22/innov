import os

DEBUG = True

TEST_ENV = False

PORT = 8005

#======================================================================
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#======================================================================
CREDS = {
	'username' : 'root',
	'password' : 'qwerty',
	'host' : 'ds149324.mlab.com:49324',
	'ENCODING' : 'UTF8'
}
DEFAULT_ENCODING = 'utf-8'

CSRF_ENABLED = True

SECRET_KEY = "blahblahblah"