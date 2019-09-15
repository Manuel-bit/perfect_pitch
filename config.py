import os
class config:
  '''
  where the applications configuarations are
  '''
  pass

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