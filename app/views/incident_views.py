import os
import datetime
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.database import *
from app.controllers.auth_users import  encode_auth_token, token_required
from app.models.database import DatabaseConnenction
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

    invaild_data = validate_input.validate_user_input(username, first_name, last_name, other_name, email, password)
    if invaild_data:
      return jsonify({
        "status":400,
        "message": invaild_data
      })

    user = db.create_user(username, first_name, last_name, other_name, email, generate_password_hash(password))
    if user:
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
  passwd = data.get('password', None)

  invalid_user = validate_input.validate_login_input(username, passwd)
  if invalid_user:
    return jsonify({
      "status":400,
      "message": invalid_user
    })

  db_user = db.get_user(username)
  if db_user and check_password_hash(db_user["password"],passwd):
    token = encode_auth_token(username).decode()
    return jsonify({
      "status": 200,
      "token": token,
      "message":"Login Successful"
    }), 200
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

  invalid_create_input = validate_input.validate_create_input(created_by, incident_type, location,          phone_number, status, images,videos, comment) 
  if invalid_create_input:
    return jsonify({
      "status": 400,
      "message":invalid_create_input
    }),400

  db_Incident = db.create_incident(created_by, incident_type, location, phone_number, status, images, videos, comment, created_on)
  if db_Incident:
    return jsonify({
      "status":200,
      "message": "Incident created successfully",
      "data":db_Incident
    })
  return jsonify({
    "status":500,
    "message": "Something went wrong."
  })
  
@redflag.route('/incident', methods=['GET'])
@token_required
def fetch_all_incident(current_user):
  db_fetch = db.fetch_all_incident()
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
      }),400
   
    
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
    