import os
import datetime
from flask import Blueprint, request, jsonify
from app.models.database import *
from app.controllers.auth_users import  encode_auth_token, token_required
from app.controllers.validations import Validators


redflag = Blueprint('redflag', __name__)

db = DatabaseConnenction()
validate_input = Validators()


required_status = ['resolved','rejected','draft','under investaging']

@redflag.route('/', methods=['GET'])
def home():
  return jsonify({
    "message": "Welcome"
  })

@redflag.route('/auth/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    
    username = data.get('username',None)
    first_name = data.get('first_name',None)
    last_name = data.get('last_name', None)
    other_name = data.get('other_names', None)
    email = data.get('email', None)
    password = data.get('password', None)

    user = db.create_user(username, first_name, last_name, other_name, email, password)
    return jsonify({
      "status": 201,
      "message":"User created successfully",
      "data":user
    }), 201
    return jsonify({
      "status":400,
      "message":"Please provide valid information "
    })

@redflag.route('/auth/login', methods=['POST'])
def login():
  data = request.get_json(force=True)
  username = data.get('username', None)
  password = data.get('password', None)

  if  not type("username") == str:
    return jsonify({
      "status": 400,
      "message":"Please make username a string"
      }), 400

  if  not type("password") == str:
    return jsonify({
      "status": 400,
      "message":"Please make password a string"
      }), 400

  if len(username) < 3:
    return jsonify({
      "status":400,
      "message":"Username too short, should have atleast 3 character"
      }), 400

  if len(password) < 5:
      return jsonify({
        "status":400,
        "message":"Password too short, should have atleast 5 character"
        }), 400
        
  db_user = db.get_user(username, password)
  if  db_user:
    token = encode_auth_token(username).decode()
    return jsonify({
      "status":200,
      "token": token,
      "message":"Login Successful"
    })
  return jsonify({
        "status": 400,
        "message":"User doesnot exit"
        }), 400
    
  
  
@redflag.route('/incident', methods=['POST'])
@token_required
def create_incident_redflag(current_user):
  data = request.get_json(force=True)

  created_by = data.get('created_by', None)
  incident_type = "redflag"
  location = data.get('location', None)
  phone_number = data.get('phone_number', None)
  status = 'draft'
  images = data.get('images', None)
  videos = data.get('videos', None)
  comment = data.get('comment', None)
  created_on = datetime.datetime.now()

  db_Incident = db.create_incident(created_by, incident_type, location, phone_number, status, images, videos, comment, created_on)
  return jsonify({
    "status":200,
    "message": "Incident created successfully",
    "data":db_Incident
  })

  #  """validatate for the input data"""

  if "created_by" not in db_Incident:
    return jsonify({
      "status": 400,
      "message":"Please fill the created_by field"
      }), 400

  if "incident_type" not in db_Incident:
    return jsonify({
      "status":400,
      "message":"Please fill in the incident_type field"
      }), 400

  if "location" not in  db_Incident:
    return jsonify({
      "status": 400,
      "message":"Please fill the location field"
      }), 400

  if "phone_number" not in  db_Incident:
    return jsonify({
      "status": 400,
      "message":"Plesae provide the phone_number"
      }), 400

  if "status" not in  db_Incident:
    return jsonify({
      "status": 400,
      "message":"Please fill the status field"
          }), 400

  if "images" not in  db_Incident:
    return jsonify({
      "status": 400,
      "message":"Please provide some images"
      }), 400

  if "videos" not in  db_Incident:
    return jsonify({
      "status": 400,
      "message":'Please provide some videos'
      }), 400

  if "comment" not in  db_Incident:
    return jsonify({
      "status": 400,
      "message":"Please leave a comment"
      }), 400

  if not type(created_by) == str:
    return jsonify({
      "status":400,
      "message":"Created_by feild must be a string"
      }), 400

  if not type(incident_type) == str:
    return jsonify({
      "status": 400,
      "message":'Incident field must be put in a string'
      }), 400

  if not type(phone_number) == int:
    return jsonify({
      "status":400,
      "message":"Phone number must be an integer"  
    }), 400

  if not type(images) == str:
    return jsonify({
      "status":400,
      'message':'Images must be put in Strings'
      }), 400
  if not type(videos) == str:
    return jsonify({
      "status": 400,
      'message':'Videos must be put in strings'
      }), 400

  if not type(comment) == str:
    return jsonify({
      "status": 400,
      "message": "Comment must be put in a string"
      }), 400
  
@redflag.route('/incident', methods=['GET'])
@token_required
def fetch_all_incident(current_user):
  db_fetch = db.fetch_all_incident()
  print(db_fetch)
  return jsonify({
    "status":200,
    "data": db_fetch
    }), 200
  
@redflag.route('/incident/<int:incident_id>', methods=['GET'])
@token_required
def get_specific(current_user, incident_id):
  db_speci = db.get_a_specific_incident(incident_id)
  return jsonify({
    "status":200,
    "data":db_speci
  }), 200

@redflag.route('/incident/<int:incident_id>/location', methods=['PATCH'])
@token_required
def update_location(current_user, incident_id):
  data = request.get_json(force=True)
  location = data.get('location', None)
  # if current_user['admin']:
  if not isinstance(location, str):
    return({
      "status": 400,
      "message": "Location should be a string"
    })

  if len(location) == 0:
    return jsonify({
      "status":400,
      "message": "Location should not be empty"
    })

  try:
    update_loc = db.update_location(incident_id, location)
    return jsonify({
      "status": 200,
      "message": "Updated incident record location: {}".format(location),
      "data": update_loc
      }), 200
  except:
    return jsonify({
      "status":400,
      "message":"Location is not provided"
      })
   
    
@redflag.route('/incident/<int:incident_id>/comment', methods=["PATCH"])
@token_required
def updated_comment(current_user, incident_id):
  data = request.get_json(force=True)
  comment = data.get('comment', None)

  if not isinstance(comment, str):
    return jsonify({
      "status": 400,
      "message": "Please comment must be a string"
    }), 400

  if len(comment) == 0:
    return jsonify({
      "status": 400,
      "message": "Comment must not be empty "
    })
  
  # if current_user['admin'] is True:
  try:
    update_com = db.update_comment(incident_id, comment)
    return jsonify({
      "status": 200,
      "message": "Updated incident record's Comment",
      "data": update_com
      }), 200
  except:
    return jsonify({
      "status": 400,
      "message": "Comment is not provided"
  }), 400
  

@redflag.route('/incident/<int:incident_id>', methods=['DELETE'])
@token_required
def delete_a_specific_incident(current_user, incident_id):
  current_user['admin'] 
  if current_user is True:
    incidenti = db.delete_incident(incident_id)
    return jsonify({
      "status": 200,
      "message": "Incident record has been deleted"
      }),200
  return jsonify({
    "status": 400,
    "message": "You donot have access for the request"
    }), 400