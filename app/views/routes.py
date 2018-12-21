from flask import Blueprint, request, jsonify
from app.models.user import User
from app.models.incident import Incident


redflag = Blueprint('create', __name__)
user_list = []
incident_list = []
required_status = ['resolved','rejected','draft','under investaging']

@redflag.route('/', methods=['GET'])
def home():
  return jsonify({
    "message": "Welcome"
  })

@redflag.route('/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    username = data.get('username', None)
    email = data.get('email', None)
    password = data.get('password', None)
    first_name = data.get('first_name', None)
    last_name = data.get('last_name', None)
    other_names = data.get('other_names', None)
    phone_number = data.get('phone_number', None)
    is_admin = data.get('is_admin', None)

    if not username or not password or not email:
        return jsonify({
        "status": 400,
        "error": "Please provide the required fields"
    }), 400

    for user in user_list:
      if username == user.username:
        return jsonify({
          "status": 400,
          "error": "Account already exits"
        }), 400

    user = User(username, first_name, last_name, other_names, email, phone_number, password, is_admin)
    user_list.append(user)

    response = {
      "status": 201,
      "message": "User account created successfully",
      "data": [user.to_dict()]
    }
    return jsonify(response), 201


@redflag.route('/login', methods=['POST'])
def login():
  data = request.get_json(force=True)
  username = data.get('username', None)
  password = data.get('password', None)

  for user in user_list:
    if username == user.username and password == user.password:
      return jsonify({
        "status": 200,
        "message": "Login successful",
        "data": [user.to_dict()]
      }), 200

  return jsonify({
    "status": 400,
    "error": "Invaild username or password"
  }), 400


@redflag.route('/incident', methods=['POST'])
def create_incident():
  data = request.get_json(force=True)

  created_by = data.get('created_by', None)
  incident_type = data.get('incident_type', None)
  location = data.get('location', None)
  phone_number = data.get('phone_number', None)
  status  = 'draft'
  images = data.get('images', None)
  videos = data.get('videos', None)
  comment = data.get('comment', None)

  incident = Incident(created_by, incident_type, location, status, images, videos, comment)
  respo = validate_incident(incident)

  if respo:
    return jsonify(respo), 400

  incident_list.append(incident)

  response = {
    "status": 201,
    "message": "Incident created successfully ",
    "data": [incident.to_dict()]
  }
  
  return jsonify(response), 201

def validate_incident(incident):
  errors = []
  user_exists = False

  if incident:
    created_by = incident.created_by
    incident_type = incident.incident_type
    location = incident.location
    status = incident.status
    images = incident.images
    videos = incident.videos

    for user in user_list:
      if created_by == user.username:
        user_exists = True
      break

    if not user_exists:
      errors.append({
        "user": "User assigned doesnot exist"
      })

    if not location:
      errors.append({
        "location_error": "Location is missing"
      })

    if not created_by:
      errors.append({
        "error_created": "Please provide valid fields"
      })

    if not incident_type:
      error.append({		
        "incident_type": "Please specify the incident type"
      })

  else:
    errors.append({
      "error": "Please provide incident details"
    })

  if len(errors) > 0:
    return {
      "status": 400,
      "errors": errors
    }
  else:
   return None
