from unittest import TestCase
from app import create_app
from app.views import incident_views 


class BaseTestCase(TestCase):
  def setUp(self):
    self.app = create_app('testing')
    self.app_context = self.app.app_context()
    self.app_context.push()
    self.client = self.app.test_client()
    self.create_user = {
                "username" : "jenny",
                "email": "jenny@gmail.com", 
                "password": "password",
                "first_name": "zawal",
                "last_name": "jenni",
                "other_names":"deal",
                "phone_number": "0708494848", 
                "is_admin": False
            } 

  def tearDown(self):
    self.app = self.app_context.pop()
    incident_views.userlist = []
    incident_views.incidentlist = []
       