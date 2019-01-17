from flask import Blueprint, request, jsonify
from app.models.user import User,user_list
from app.models.incident import Incident,incident_list


redflag = Blueprint('create', __name__)


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
        "status": 404,
        "error": "Please provide the required fields"
    }), 404

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
    "status": 404,
    "error": "Invaild username or password"
  }), 404


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
    "message": "Incident record created successfully ",
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
        "user_error": "User assigned doesnot exist"
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
      errors.append({		
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

@redflag.route('/incident', methods=['GET'])
def fetch_all_incident():
  if incident_list:
    return jsonify({
        "status": 200,
        "data": [incident.to_dict() for incident in incident_list]
      })
  return jsonify({
      "status":404,
      "message": "No incidents created"
      }), 404

@redflag.route('/incident/<incident_id>', methods=['GET'])
def get_specific(incident_id):
  for incident in incident_list:
    if incident.id == incident_id:
      return jsonify({
        "status": 200,
        "data": incident.to_dict()
      })

  return jsonify({
    "status": 404,
    "error": "Incident not found" 
    })

@redflag.route('/incident/<incident_id>/location', methods=['PATCH'])
def update_location(incident_id):
  data = request.get_json(force=True)
  location = data.get('location', None)

  if not location:
    return jsonify({
      "status": 404,
      "message": "Please include Location of the record"
    })

  for incident in incident_list:
    if incident.id == incident_id:
      incident.location = location
      return jsonify({
        "status": 200,
        "message": "Updated incident record's location",
        "data": incident.to_dict()
      })

  return jsonify({
    "status": 404,
    "message": "Incident record not created"
  })

@redflag.route('/incident/<incident_id>/comment', methods=["PATCH"])
def updated_comment(incident_id):
  data = request.get_json(force=True)
  comment = data.get('comment', None)

  if not comment:
    return jsonify({
      "status": 404,
      "message": "Please leave a comment"
    })

  for incident in incident_list:
    if incident.id == incident_id:
      incident.comment = comment
      return jsonify({
        "status": 200,
        "message": "Updated incident record's Comment",
        "data": incident.to_dict()
      })

  return jsonify({
    "status": 404,
    "message": "Incident record not created"
  })

@redflag.route('/incident/<incident_id>', methods=['DELETE'])
def delete_a_specific_incident(incident_id):
  for incident in incident_list:
    if incident.id == incident_id:
      incident_list.remove(incident)
      return jsonify({
        "status": 200,
        "message": "Incident record has been deleted"
      })
  return jsonify({
    "status": 404,
    "message": "Incident record not created"
    })
