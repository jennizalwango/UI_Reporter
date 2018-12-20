from flask import Blueprint, request, jsonify
from app.models.user import User


redflag = Blueprint('create', __name__)
user_list = []

@redflag.route('/register', methods=['POST'])
def register():
    data = request.get_json(force = True)
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


# @redflag.route('/')
