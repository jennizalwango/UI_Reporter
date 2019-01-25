from unittest import TestCase
from app.views import incident_views
from app.models.database import DatabaseConnenction
from unittest import TestCase
from app.views.incident_views import *
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
        self.db.drop_table_users()


# class BaseTestCase(TestCase):
#     def setUp(self):
#         self.client = app.test_client()
#         self.db = DatabaseConnenction()
#         self.create_user()
#         self.create_incident()
       
    
#     def tearDown(self):
#         self.db.truncate_tables()
    

#     def create_user(self):
#         query = """INSERT INTO users (user_id, username, first_name, last_name, other_name, email, password)
#         VALUES(2, 'jenny', 'jenny', 'zalwango','elizabeth','jenny@gmil.com','pbkdf2:sha256:50000$cdVO7aZw$316fe667df3c22da936ca9cbe513e828903d5d5727c938a943b34ff682d35f44');"""
#         self.db.cursor.execute(query)

#     def create_incident(self):
#         query1 = """INSERT INTO incident (incident_id, created_by, incident_type, location, phone_number, status, images, videos, comment,)
#         VALUES(1, 2, 'redflag', 'bugolobi','0706373532','draft', 'nice.jpeg', 'hes.mp4','Nice');"""
#         self.db.cursor.execute(query1)

#         query2 = """INSERT INTO incident (incident_id, created_by, incident_type, location, phone_number, status, images, videos, comment,)
#         VALUES(2, 2, 'intervention', 'bugaya','0706473532','draft', 'tree.jpeg', 'cry.mp4','fair');"""
#         self.db.cursor.execute(query2)

#         query3 = """INSERT INTO incident (incident_id, created_by, incident_type, location, phone_number, status, images, videos, comment,)
#         VALUES(3, 2, 'intervention', 'kasara','07046873532','draft', 'real.jpeg', 'fake.mp4','good');"""
#         self.db.cursor.execute(query3)
