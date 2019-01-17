from unittest import TestCase
from app import create_app
from app.models.incident import incident_list


class BaseTestCase(TestCase):
  def setUp(self):
    self.app = create_app('testing')
    self.app_context = self.app.app_context()
    self.app_context.push()
    self.client = self.app.test_client()

  def tearDown(self):
    self.app = self.app_context.pop()
    incident_list.clear()
    