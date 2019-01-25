from flask import json
from app.tests.base import BaseTestCase



class APITestCase(BaseTestCase):

    def test_index(self):
       with self.client:
           response = self.client.get('/api/v2/', content_type='application/json')
           self.assertEqual(response.status_code, 200)
        
    def test_register_user(self):
       with self.client:
            response = self.client.post('api/v2/auth/register', data=json.dumps(self.create_user), content_type='application/json')
            self.assertEqual(response.status, '201 CREATED')
         
    
    def test_login_user_sucessful(self):
        with self.client:
            login_user = {
                "username":"jenny",
                "password": "password"
            }
            response = self.client.post('api/v2/auth/register', data=json.dumps(self.create_user),content_type='application/json') 
            response = self.client.post('/api/v2/auth/login', data=json.dumps(login_user), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            result = json.loads(response.data.decode())
            self.assertEqual(result['message'], "Login Successful")

    def test_create_incident(self):
        with self.client:
            self.client.post('/api/v2/register', data=json.dumps(self.create_user),content_type='application/json')
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
            response = self.client.post('/api/v2/incident', data=json.dumps(incident_data), content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_invalid_user(self):
        with self.client:
            login_user = {
                "username":"jen",
                "password": "passwor"
            }
            response = self.client.post('api/v2/auth/login', data=json.dumps(login_user),content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_update_location(self):
        with self.client:
            update_data = {
                "location":"bugaya"
            }
            response = self.client.patch('api/v2/incident/1/location', data=json.dumps(update_data), content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_update_comment(self):
        with self.client:
            update_data_comment = {
                "comment":"Fairly"
            }
            response = self.client.patch('api/v2/incident/1/comment', data=json.dumps(update_data_comment), content_type='application/json')
            self.assertEqual(response.status_code, 200)

    
   
    