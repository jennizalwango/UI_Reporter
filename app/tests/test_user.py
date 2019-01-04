from flask import json
from app.tests.base import BaseTestCase


class APITestCase(BaseTestCase):

    def test_register_user(self):
       with self.client:
            user = {
                "username" : "jenny",
                "email": "jenny@gmail.com", 
                "password": "password",
                "first_name": "zawal",
                "last_name": "jenni",
                "other_names":"deal",
                "phone_number": "0708494848", 
                "is_admin": False,
            }
            response = self.client.post('/api/v1/register', data=json.dumps(user), content_type='application/json')
            data = json.loads(response.data.decode())
            self.assertEqual("User account created successfully", data["message"])
            self.assertEqual(201, response.status_code)

    def test_required_fields(self):
        with self.client:
            response = self.client.post('/api/v1/register', data=json.dumps({}), content_type='application/json')
            results = json.loads(response.data.decode())
            print(results)
            self.assertEqual("Please provide the required fields", results["error"])
            self.assertEqual(400, response.status_code)

    def test_login_user_sucessful(self):
        with self.client:
            user = {
                "username":"jenny",
                "password": "12345"
            }
            response = self.client.post('/api/v1/login', data=json.dumps(user), content_type='application/json')
            data = json.loads(response.data.decode())
            self.assertEqual("Login Successful", data['message'])
            self.assertEqual(200, response.status_code)

    def test_login_invalid(self):
        with self.client:
            login_data ={
                "username": "jenny",
                "password": "12345"
            }
            response = self.client.post('/api/v1/login', data=json.dumps(login_data),content_type='application/json')
            results = json.loads(reponse.data.decode())
            print(results)
            self.assertEqual("Invalid username or password",results["error"])
            self.assertEqual(400, response.stauts_code)

    def test_created_incident(self):
        with self.client:
            create_user = {
                "username" : "jenny",
                "email": "jenny@gmail.com", 
                "password": "password",
                "first_name": "zawal",
                "last_name": "jenni",
                "other_names":"deal",
                "phone_number": "0708494848", 
                "is_admin": False,
            }

            incident_data = {
                "created_by": "jenny", 
                "incident_type": "redflag",
                "location": "bukoto",
                "phone_number": "0726725271",
                "status": "draft",
                "images":"come.jpg",  
                "videos":"go.png",
                "comment":"fair",
            }
            response = self.client.post('/api/v1/incident', data=json.dumps(incident_data), content_type='application/json')
            data = json.loads(response.data.decode())
            print(data)
            self.assertEqual("Incident created successfully", data["message"])
            self.assertEqual(201, response.status_code)

    def test_user_not_exits(self):
        with self.client:
            incident_data = {
                "created_by": "joan",
                "incident_type": "redflag",
                "location": "bukoto",
                "phone_number": "0703789731",
                "status": "draft",
                "images": "nice.jeg",
                "videos": "ice.jpg",
                "comment": "nice",
            }
            response = self.client.post('/api/v1/incident', data=json.dumps(incident_data), content_type='application/json')
            data = json.loads(response.data.decode())
            self.assertEqual(400, response.status_code)


            self.assertEqual("User assigned doesnot exist", data['message'])
            