from unittest import TestCase
from app.views import incident_views
from app.models.database import DatabaseConnenction
from app import app


class BaseTestCase(TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.db = DatabaseConnenction()
        self.db.create_tables()
        self.create_user = {
            "username": "jenny",
            "email": "jenny@gmail.com",
            "password": "password",
            "first_name": "zawal",
            "last_name": "jenni",
            "other_names": "deal",
            "phone_number": "0708494848",
            "is_admin": False
        }

        self.create_incident = {
            "created_by": "jenny",
            "incident_type": "redflag",
            "location": "jinja",
            "phone_number": "070367235",
            "status": "draft",
            "images": "come.jpg",
            "videos": "go.mp4",
            "comment": "nice"
        }
        self.login_data = {
            "username": "jenny",
            "password": "12345"
        }

        self.required_feilds = {
            "username": "",
            "email": "",
            "password": "",
            "first_name": "",
            "last_name": "",
            "other_names": "",
            "phone_number": "",
            "is_admin": "",
        }

    def tearDown(self):
        self.db.drop_tables()
