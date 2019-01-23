from flask import Blueprint, request, jsonify
import datetime
from app.models.database import *
import os
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from app.controllers.validations import Validators
from app.controllers.user_controllers import get_user

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

    
    db.create_tables()
    check_email = db.check_email(email)
    if check_email:
      return jsonify({
        "status": 400,
        "message":"Email already taken" 
      })
    invalid_email = validate_input.validatate_user_email(email)
    if invalid_email:
      return jsonify({
        "status": 400,
        "error": invalid_email
      }), 400

    invalid_username = validate_input.validatate_user_username(username)
    if invalid_username:
      return jsonify({
        "status": 400,
        "error": invalid_username
      }), 400

    invalid_first_name = validate_input.validate_user_first_name(first_name)
    if invalid_first_name:
      return jsonify({
        "status": 400,
        "error": invalid_first_name
      }), 400

    invalid_last_name = validate_input.validate_user_last_name(last_name)
    if invalid_last_name:
      return jsonify({
        "status": 400,
        "error": invalid_last_name
      }), 400

    invalid_other_name = validate_input.validate_user_other_name(other_name)
    if invalid_other_name:
      return jsonify({
        "status": 400,
        "error": invalid_other_name
      }), 400


    user = db.create_user(username, first_name, last_name, other_name, email, password)
    return jsonify({
      "status": 201,
      "message":"User created successfully",
      "data":user
    }), 201

@redflag.route('/auth/login', methods=['POST'])
def login():
  data = request.get_json(force=True)
  username = data.get('username', None)
  password = data.get('password', None)

  db_user = db.get_user(username, password)
  if not db_user:
    return jsonify({
      "status": 400,
      "message":"User doesnot exit"
      }), 400
  return jsonify({
    "status":200,
    "message":"Login Successful"
  })
  if  not type ("username") == str:
    return jsonify({
      "status": 400,
      "message":"Please make username a string"
      }), 400

  if  not type ("password") == str:
    return jsonify({
      "status": 400,
      "message":"Please make password a string"
      }), 400

@redflag.route('/incident', methods=['POST'])
# @jwt_required
def create_incident_redflag():
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

  # current_user = get_jwt_identity()
  # if current_user['admin'] != False:
  #   return jsonify({
  #     "status":400,
  #     "message":"You donot have access to this function",
  #     "data":db_Incident
  #     }), 400

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

#  """validations for the input data"""

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

  # db.incident(current_user['id'], created_by, incident_type, location, phone_number,status, images, videos, comment)
  
@redflag.route('/incident', methods=['GET'])
# @jwt_required
def fetch_all_incident():
  db_fetch = db.fetch_all_incident()
  return jsonify({
    "status":200,
    "data": db_fetch
    }), 200

    # """acessed if admin"""

  # current_user = get_jwt_identity()

  # if current_user['admin'] == True:
  #     incidents = db.fetch_all_incident()
  # else:
  #     """ by user """
  #     incidents = db.fetch_all_incident(current_user['id'])

  
@redflag.route('/incident/<int:incident_id>', methods=['GET'])
@jwt_required
def get_specific(incident_id):
  current_user = get.get_jwt_identity

  incident = db.get_a_specific('incident_id', id)
  if not indicent:
    return jsonify({
      "status":400,
      "message" : "Incident  not found"
      }), 400

  if current_user['admin'] == True or current_user['id'] == incident[2]:
    return jsonify({
      "status":200,
      "message": incidents_in
      }), 200

  return jsonify({
    "status":400,
    "message" : "You have not created incidents"
    }), 400

@redflag.route('/incident/<int:incident_id>/location', methods=['PATCH'])
# @jwt_required
def update_location(incident_id):
  data = request.get_json(force=True)
  location = data.get('location', None)
  
  update_loc = db.update_location(incident_id, location)
  return jsonify({
    "status": 200,
    "message": "Updated incident record location: {}".format(location),
    "data": update_loc
    }), 200


  # if location not in list(data.keys()):
  #   return jsonify({
  #     "status": 400,
  #     "message": "Please include Location of the record"
  #   }), 400

  # if not type(location) == str:
  #   return jsonify({
  #     "status": 400,
  #     "message":"Location record should be a string"
  #     }), 400
  # if not location.strip():
  #   return jsonify({
  #     "status":400,
  #     "message":"Please include Location of the record"
  #     }), 400
  
  # current_user = get_jwt_identity()
  # if current_user['id'] != db.get_user_id(id):
  #   return jsonify({
  #     "ststus":400,
  #     "message":"Sorry you cannot access this endpoint"
  #   })
    
@redflag.route('/incident/<int:incident_id>/comment', methods=["PATCH"])
def updated_comment(incident_id):
  data = request.get_json(force=True)
  comment = data.get('comment', None)

  update_com = db.update_comment(incident_id, comment)
  if not comment:
    return jsonify({
      "status": 400,
      "message": "Please leave a comment"
    }), 400
  return jsonify({
        "status": 200,
        "message": "Updated incident record's Comment",
        "data": update_com
      }), 200

  return jsonify({
    "status": 400,
    "message": "Incident record not created"
  }), 400



@redflag.route('/incident/<int:incident_id>/comment', methods=["PATCH"])
def updated_comment(incident_id):
  data = request.get_json(force=True)
  comment = data.get('comment', None)

  update_com = db.update_comment(incident_id, comment)
  if not comment:
    return jsonify({
      "status": 400,
      "message": "Please leave a comment"
    }), 400
  return jsonify({
        "status": 200,
        "message": "Updated incident record's Comment",
        "data": update_com
      }), 200
@redflag.route('/incident/<int:incident_id>', methods=['DELETE'])
def delete_a_specific_incident(incident_id):

  # current_user = jwt_get_identity()
  # current_user['admin'] == True
  incidenti = db.drop_tables()
  return jsonify({
    "status": 200,
    "message": "Incident record has been deleted"
    }),200
  return jsonify({
    "status": 400,
    "message": "Incident record not created"
    }), 400