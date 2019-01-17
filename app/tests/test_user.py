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
            self.assertEqual(404, response.status_code)

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
            self.assertEqual(response.status_code, 200)
            results = json.loads(response.data.decode())
            self.assertIn("Login successful", results["message"] )

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

            login_data = {
                "username": "jenny",
                "password": "12345"
            }
            response = self.client.post('/api/v1/login', data=json.dumps(login_data),content_type='application/json')
            self.assertEqual(response.status, '404 NOT FOUND')
            results = json.loads(response.data.decode())
            self.assertIn("Invaild username or password", results["error"])
            

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

    def test_location_missing(self):
        with self.client:
            incident_data = {
                "created_by": "joan",
                "incident_type": "redflag",
                "phone_number": "0703789731",
                "status": "draft",
                "images": "nice.jeg",
                "videos": "ice.jpg",
                "comment": "nice",
            }
            response = self.client.post('/api/v1/incident', data=json.dumps(incident_data),content_type='application/json')
            self.assertEqual(response.status_code, 400)
            results = json.loads(response.data.decode())
            self.assertIn("Location is missing", str(response.data))

    def test_incident_type_missing(self):
        with self.client:
            incident_data = {
                "created_by": "joan",
                "location": "bukoto",
                "phone_number": "0703789731",
                "status": "draft",
                "images": "nice.jeg",
                "videos": "ice.jpg",
                "comment": "nice",
            }
            response = self.client.post('/api/v1/incident', data=json.dumps(incident_data),content_type='application/json')
            self.assertEqual(response.status_code, 400)
            results = json.loads(response.data.decode())
            self.assertIn("Please specify the incident type", str(response.data))

    def test_created_by_missing(self):
        with self.client:
            incident_data = {
                "incident_type": "redflag",
                "location": "bukoto",
                "phone_number": "0703789731",
                "status": "draft",
                "images": "nice.jeg",
                "videos": "ice.jpg",
                "comment": "nice",
            }
            response = self.client.post('/api/v1/incident', data=json.dumps(incident_data),content_type='application/json')
            self.assertEqual(response.status_code, 400)
            results = json.loads(response.data.decode())
            self.assertIn("Please provide valid fields", str(response.data))

    # def test_incident_details_missing(self):
    #     with self.client:
    #         incident_data = {

    #         }
    #         response = self.client.post('/api/v1/incident', data=json.dumps(incident_data),content_type='application/json')
    #         self.assertEqual(response.status_code, 400)
    #         results = json.loads(response.data.decode())
    #         self.assertIn("Please provide incident details", str(response.data))   
            
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
            self.client.post('/api/v1/incident', data=json.dumps(incident_data))
            response = self.client.get('/api/v1/incident/1', content_type='application/json')
            self.assertEqual(response.status_code, 200)

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
            self.client.post('/api/v1/incident', data=json.dumps(incident_data))
            response = self.client.get('/api/v1/incident', content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_no_incident_exits(self):
        with self.client:
            response = self.client.get('/api/v1/incident', content_type='application/json')
            self.assertEqual(response.status_code, 404)
            results = json.loads(response.data.decode())
            self.assertIn("No incidents created", results["message"] )
            


    def test_update_location(self):
        with self.client:
            incident_data = {
                "location": "bukoto"
            }
            response =self.client.patch('/api/v1/2/location',data=json.dumps(incident_data), content_type='application/json')
            self.assertEqual(response.status_code, 404)

    def test_update_comment(self):
        with self.client:
            incident_data = {
                "comment": "Fair"
            }
            response = self.client.patch('/api/v1/3/comment',data=json.dumps(incident_data), content_type='application/json')
            self.assertEqual(response.status_code,404)

    def test_delete_a_specific_incident(self):
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
            response = self.client.delete('/api/v1/incident/1', data=json.dumps(incident_data), content_type='application/json')
            self.assertEqual(response.status_code, 200)
