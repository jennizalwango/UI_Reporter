import uuid
from datetime import datetime

class User:
  def __init__(self, username, first_name, last_name, other_names, email, phone_number, password, is_admin):
    self.id = str(uuid.uuid4())
    self.username = username
    self.email = email
    self.password = password
    self.first_name = first_name
    self.last_name = last_name
    self.other_names = other_names
    self.phone_number = phone_number
    self.registered = datetime.now()
    self.is_admin  = is_admin

  def to_dict(self):
    return self.__dict__

  def __to__str(self):
    return str(self.to_dict())
