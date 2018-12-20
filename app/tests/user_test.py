from flask import json
from app.test.base import BaseTestCase


class APITestCase(BaseTestCase):

    def test_register_successfully(self):
        with self.client:
            self.user = {
                "username": "jenny",
                "email": "jenny@gmail",
                "password": "password"
            }
            response = self.client.post('/api/v1/register',data=json.dumps(self.user), content_type='application/json')
            data = json.loads(response.data.decode())
            print(data)
            self.assertEqual("User registered successfully", data["message"])
            self.assertEqual(201, response.status_code)

   def test_Please_provide_the_required_fields(self):
         with self.client:
             user_dict1 = self.user
             del user_dict1["username","password","email"]
             response =  self.client.post('/api/v1/register', results = json.dumps(user_dict1),content_type='application/json')
             results = json.loads(response.results.decode())
             print(results)
             self.assertEqual("Please provide the required fields",results["error"])
             self.assertEqual(400,response.status_code)
