import os

class Config:
  DEBUG = False
  TESTING = False
  SECRET_KEY = os.environ.get('SECRET_KEY', "1Nrd2JFQIWAh3aa0q9zrN15www7Czc6Q")


class ProductionConfig(Config):
  pass


class DevelopmentConfig(Config):
  DEBUG = True
  

class TestingConfig(Config):
  TESTING = True


configuration = {
  "development": DevelopmentConfig,
  "production": ProductionConfig,
  "testing": TestingConfig
}
