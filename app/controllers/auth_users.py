import datetime
import jwt
from flask import request, jsonify
from functools import wraps
from app.models.database import DatabaseConnenction
from app.config import configuration


SECRET_KEY = configuration["production"].SECRET_KEY
db = DatabaseConnenction()


def encode_auth_token(password):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub': password
        }
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as error:
        return error

def token_required(func):
  @wraps(func)
  def decorated(*args, **kwargs):
    token = None
    if 'Authorization' in request.headers:
      token = request.headers['Authorization']

    if not token:
      return jsonify({
        "status": 400,
        "message": "Token  missing"
        })

    try:
      data = jwt.decode(token, SECRET_KEY)
      current_user = db.get_user_by_password(password=data["sub"])
      
    except:
      return jsonify({
        "status": 401,
        "meassage": "Token Invalid"
        })
    return func(current_user, *args, **kwargs)

  return decorated
