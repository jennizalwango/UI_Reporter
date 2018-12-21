from flask import Flask
from app.config import configuration

def create_app(environment):
  app = Flask(__name__)
  app.config.from_object(configuration.get(environment))

  from app.views.routes import redflag
  
  app.register_blueprint(redflag, url_prefix="/api/v1")
  return app
