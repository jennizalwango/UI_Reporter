
from datetime import datetime
import uuid

class Incident:
  def __init__(self, created_by, incident_type, location, status, images, videos, comment):
    self.id = str(uuid.uuid4())
    self.created_on = datetime.now()
    self.created_by = created_by
    self.incident_type = incident_type
    self.location = location
    self.status = status
    self.images = images
    self.videos = videos
    self.comment = comment

  def to_dict(self):
    return self.__dict__ 

  def __to_str(self):
    return str(self.to_dict())
