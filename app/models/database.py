import psycopg2
from psycopg2.extras import RealDictCursor
 

class DatabaseConnenction:
  def __init__(self):
    connection_details = """ dbname='jenny' user='postgres' password='postgres'  port='5432' host='localhost'   
    """
    try:
        self.connection = psycopg2.connect(connection_details)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        print('Connected to database')
        # self.create_tables()

    except:
      print('Failed to connect to database')

  def create_tables(self):
    """create database tables"""
    create_user_table = """CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY, username VARCHAR(50), first_name VARCHAR(50), last_name VARCHAR(50),other_name VARCHAR(50), email VARCHAR(50),password VARCHAR(100), admin BOOLEAN DEFAULT FALSE);"""
    self.cursor.execute(create_user_table)
    
    create_incident_table = "CREATE TABLE IF NOT EXISTS incident\
    ( incident_id SERIAL PRIMARY KEY, created_by SERIAL REFERENCES users(user_id), incident_type VARCHAR(50), \
    location VARCHAR(50), phone_number VARCHAR(50),status VARCHAR(50), images VARCHAR(50), videos VARCHAR(50), comment VARCHAR(50), created_on VARCHAR(50));"
    self.cursor.execute(create_incident_table)

  def create_user(self, username, first_name, last_name, other_name, email, password):
    query = """
      INSERT INTO users (username, first_name, last_name, other_name, email, password)
      VALUES('{}', '{}', '{}', '{}','{}','{}') RETURNING user_id,username,first_name,last_name, other_name, email ;""".format(username, first_name, last_name, other_name, email, password)
    self.cursor.execute(query)
    return self.cursor.fetchall()

  def get_user(self,username, password):
    query = "SELECT username, password, user_id FROM users WHERE  username = '{}'AND password = '{}';".format(username, password)
    self.cursor.execute(query)
    user_in = self.cursor.fetchone()
    return user_in

  def get_user_by_password(self, password):
    query = "SELECT password FROM users WHERE  password = '{}';".format(password)
    self.cursor.execute(query)
    userz = self.cursor.fetchone()
    return userz

  # def login_user(self, username, password):
  #   query = "INSERT INTO user(username, password VALUES('{}','{}'));RETURNING  user_id;"" .format(username, password)
  #   self.cursor.execute(query)
    
  def get_user_id(self, id):
    query = "SELECT user_id FROM incident WHERE incident_id = '{}';".format(id)
    self.cursor.execute(query)
    user_id = self.cursor.fetchone()[0]
    return user_id

  def check_email(self, email):
    query = "SELECT * FROM users WHERE email = '{}';".format(email)
    self.cursor.execute(query)
    emaile = self.cursor.fetchone()
    return emaile

  def create_incident(self, created_by, incident_type, location, phone_number, status, images, videos, comment,created_on):
    query = "INSERT INTO incident(created_by, incident_type, location, phone_number, status, images, videos,comment, created_on)\
    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}') RETURNING * ".format(created_by, incident_type, location, phone_number, status, images, videos, comment, created_on)
    self.cursor.execute(query)
    return self.cursor.fetchall()
  
  def fetch_all_incident(self):
    query = "SELECT * FROM incident;"
    self.cursor.execute(query)
    incidents_in = self.cursor.fetchall()
    return incidents_in

  def get_a_specific_incident(self, incid_id):
    query = "SELECT * FROM incident WHERE incident_id ={};".format(incid_id)
    self.cursor.execute(query)
    incidents_in = self.cursor.fetchall()
    return incidents_in

  def update_location(self, incident_id, location):
    query = "UPDATE incident SET location = '{}' WHERE incident_id = '{}'RETURNING * ;".format(location, incident_id)
    self.cursor.execute(query)
    return self.cursor.fetchall()

  def update_user(self, user_id, value):
    query = "UPDATE users SET admin = '{}' WHERE user_id = '{}'RETURNING * ;".format(value, user_id)
    self.cursor.execute(query)
  
    
  def update_status(self, incident_id, status):
    query = "UPDATE incident SET status = '{}' WHERE incident_id = '{}';".format(status, incident_id)
    self.cursor.execute(query)

  def update_comment(self, incident_id, comment):
    query = "UPDATE incident SET comment = '{}' WHERE incident_id = '{}' RETURNING *;\
    ".format(comment, incident_id)
    self.cursor.execute(query)
    return self.cursor.fetchone()

  def delete_incident(self, incident_id):
    query = "DELETE FROM incident WHERE incident_id = '{}' RETURNING incident_id" .format(incident_id)
    self.cursor.execute(query)
    return self.cursor.fetchone()



