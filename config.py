import os


class Config:
  '''
  where the applications configuarations are
  '''
  SECRET_KEY = os.environ.get('SECRET_KEY')

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