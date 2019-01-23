from datetime import datetime
from app.models.database import DatabaseConnenction


# class Incident:
#   def __init__(self, user_id, incident_id, created_by, incident_type, location, status, images, videos, comment):
#     self.user_id = user_id
#     self.created_on = datetime.now()
#     self.incident_id = incident_id
#     self.created_by = created_by
#     self.incident_type = incident_type
#     self.location = location
#     self.status = status
#     self.images = images
#     self.videos = videos
#     self.comment = comment

#   def to_dict(self):
#     return self.__dict__

#   def __to_str(self):
#     return str(self.to_dict())

def create_incident(self, created_by, incident_type, location, status, images, videos, comment):
  query = "INSERT INTO incident(created_by, incident_type, location, status, images, videos)\
  VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(created_by, incident_type, location, status, images, videos, comment)
  self.cursor.execute(query)

def fetch_all_incident(self):
  query = "SELECT * FROM incident;"
  self.cursor.execute(query)
  incidents_in = self.cursor.fetchall()
  return incidents_in

def get_a_specific_incident(self, id):
  query = "SELECT * FROM incident WHERE user_id = {};".format(id)
  self.cursor.execute(query)
  incidents_in = self.cursor.fetchall()
  return incidents_in

def update_location(self, incident_id, location):
  query = "UPDATE incident SET location = '{}' WHERE incident_id = '{}';".format(location, incident_id)
  self.cursor.execute(query)
  
def update_status(self, incident_id, status):
  query = "UPDATE incident SET status = '{}' WHERE incident_id = '{}';".format(status, incident_id)
  self.cursor.execute(query)

def update_comment(self, incident_id, comment):
  query = "UPDATE incident SET comment = '{}' WHERE incident_id = '{}';\
  ".format(comment, incident_id)
  self.cursor.execute(query)

def drop_tables(self):
  query = "DROP TABLE users ;DROP TABLE incident; "
  self.cursor.execute(query)
  return "Dropped"
