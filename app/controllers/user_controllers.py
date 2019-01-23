from app.models.database import DatabaseConnenction
from datetime import datetime
# class User:
#   def __init__(self, user_id, username, first_name, last_name, other_names, email, phone_number, password, admin):
#     self.user_id = user_id
#     self.username = username
#     self.email = email
#     self.password = password
#     self.first_name = first_name
#     self.last_name = last_name
#     self.other_names = other_names
#     self.phone_number = phone_number
#     self.registered = datetime.now()
#     self.admin = admin

db = DatabaseConnenction()

def create_user(username, first_name, last_name, other_name, email, password):
  query = "INSERT INTO users (username,first_name,last_name, other_name, email, password, admin) VALUES('{}', '{}', '{}', '{}', '{}', '{}', False);".format(username, first_name, last_name, other_name, email, password)
  db.cursor.execute(query)

def login_user(username, password):
  query = "INSERT INTO user(username, password VALUES('{}','{}'));" .format(username, password)
  db.cursor.execute(query)

def get_user(username, password):
  query = "SELECT username, password FROM users WHERE  username = '{}'AND password = '{}';".format(username, password)
  db.cursor.execute(query)
  user_in = db.cursor.fetchone()
  return user_in

def get_user_id(id):
  query = "SELECT user_id FROM incident WHERE incident_id = '{}';".format(id)
  db.cursor.execute(query)
  user_id = db.cursor.fetchone()[0]
  return user_id






