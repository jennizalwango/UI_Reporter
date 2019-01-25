from flask import Flask
from app.config import configuration
from app.views.incident_views import redflag

app = Flask(__name__)
app.config['SECRET_KEY'] = "1Nrd2JFQIWAh3aa0q9zrN15www7Czc6Q"
app.register_blueprint(redflag, url_prefix="/api/v2")
