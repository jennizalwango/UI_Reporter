from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import configuration
from app.views.incident_views import redflag

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = "1Nrd2JFQIWAh3aa0q9zrN15www7Czc6Q"

app.register_blueprint(redflag, url_prefix="/api/v1")

