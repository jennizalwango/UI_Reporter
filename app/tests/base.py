import unittest import TestCase
from app import create_app


class BaseTestCase(TestCase):
  def setup(self):
    self.app = create_app('testing')
    self.app_context = app.app_context()
    self.app_context.push()
    self.client = self.app.test_client()

    def TearDown(self):
      self.app = self.app_context.pop()