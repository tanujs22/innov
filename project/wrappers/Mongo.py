from pymongo import MongoClient
import config
import sys

def init(encoding=config.CREDS['ENCODING']):
	reload(sys)
	sys.setdefaultencoding(encoding)
	creds = config.CREDS
	client = MongoClient('mongodb://root:qwerty@ds149324.mlab.com:49324/innovaccer')
	return client