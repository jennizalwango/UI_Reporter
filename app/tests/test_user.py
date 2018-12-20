from flask import json
from app.tests.base import BaseTestCase


class APITestCase(BaseTestCase):

    def test_register_user(self):
        with self.client:
            self.user = {
                "username": "jenny",
                "email": "jenny@gmail",
                "password": "password"
            }
            response = self.client.post('/api/v1/register', data=json.dumps(self.user), content_type='application/json')
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
