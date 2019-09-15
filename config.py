import os


class Config:
  '''
  where the applications configuarations are
  '''
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATBASE_URI = 'postgresql+psycopg2://emmanuel:lilfranken@localhost/pitch'

class ProdConfig(Config):
  '''
  class tha tdescribes production configuarations 
  '''
  pass

class DevConfig(Config):
  DEBUG = True

config_options = {
  'development' : DevConfig,
  'production'  : ProdConfig
}