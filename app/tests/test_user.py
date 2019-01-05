from flask import json
from app.tests.base import BaseTestCase


class APITestCase(BaseTestCase):

    def test_register_user(self):
       with self.client:
            user = {
                    "username":"moses",
                    "password":"word",
                    "email":"jennyiceuy@gmail.com",
                    "first_name":"zawah",
                    "last_name":"boy",
                    "other_names":"sweets",
                    "phone_number":"0706237809",
                    "is_admin": ""
            }
            response = self.client.post('/api/v1/register', data=json.dumps(user), content_type='application/json')
            self.assertEqual(response.status,'201 CREATED')
         
    def test_required_fields(self):
        with self.client:
            response = self.client.post('/api/v1/register', data=json.dumps({}), content_type='application/json')
            results = json.loads(response.data.decode())
            print(results)
            self.assertEqual("Please provide the required fields", results["error"])
            self.assertEqual(400, response.status_code)

    def test_login_user_sucessful(self):
        with self.client:
            users = {
                "username" : "jenny",
                "email": "jenny@gmail.com", 
                "password": "password",
                "first_name": "zawal",
                "last_name": "jenni",
                "other_names":"deal",
                "phone_number": "0708494848", 
                "is_admin": False,
            }
            self.client.post('/api/v1/register', data=json.dumps(users),content_type='application/json') 

            user = {
                "username":"jenny",
                "password": "password"
            }
            
            response = self.client.post('api/v1/login', data=json.dumps(user), content_type='application/json')
            self.assertEqual(response.status_code,200)

    def test_login_invalid(self):
        with self.client:
            users = {
                "username" : "jenny",
                "email": "jenny@gmail.com", 
                "password": "password",
                "first_name": "zawal",
                "last_name": "jenni",
                "other_names":"deal",
                "phone_number": "0708494848", 
                "is_admin": False
            }
            self.client.post('/api/v1/register', data=json.dumps(users),content_type='application/json') 

            login_data ={
                "username": "jenny",
                "password": "12345"
            }
            response = self.client.post('/api/v1/login', data=json.dumps(login_data),content_type='application/json')
            self.assertEqual(response.status,'400 BAD REQUEST')
            

    def test_create_incident(self):
        with self.client:
            create_user = {
                "username" : "jenny",
                "email": "jenny@gmail.com", 
                "password": "password",
                "first_name": "zawal",
                "last_name": "jenni",
                "other_names":"deal",
                "phone_number": "0708494848", 
                "is_admin": False
            }
            self.client.post('/api/v1/register', data=json.dumps(create_user),content_type='application/json')
            incident_data = {
                "created_by": "jenny", 
                "incident_type": "redflag",
                "location": "bukoto",
                "phone_number": "0726725271",
                "status": "draft",
                "images":"come.jpg",  
                "videos":"go.png",
                "comment":"fair"
            }
            response = self.client.post('/api/v1/incident', data=json.dumps(incident_data), content_type='application/json')
            self.assertEqual(response.status_code, 201)

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
            self.assertEqual(400, response.status_code)
            
    def test_get_specific_incident(self):
        with self.client:
            incident_data = {
                "created_by": "jenny", 
                "incident_type": "redflag",
                "location": "bukoto",
                "phone_number": "0726725271",
                "status": "draft",
                "images":"come.jpg",  
                "videos":"go.png",
                "comment":"fair"
            }
            response = self.client.post('/api/v1/incident', data=json.dumps(incident_data), content_type='application/json')
            self.assertEqual(response.status_code, 201)

    def test_fetch_all_incident(self):
        with self.client:
            incident_data = {
                "created_by": "jenny", 
                "incident_type": "redflag",
                "location": "bukoto",
                "phone_number": "0726725271",
                "status": "draft",
                "images":"come.jpg",  
                "videos":"go.png",
                "comment":"fair"
            }
            response = self.client.post('/api/v1/incident', data=json.dumps(incident_data), content_type='application/json')
            self.assertEqual(response.status_code, 201)

    