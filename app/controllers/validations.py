# from app.models.database import DatabaseConnenction
# from flask import jsonify

# db = DatabaseConnenction()


class Validators:

    def validatate_user_email(self, email):
        if not email:
            return "Email field cannot be left out"

        if not "@" in email:
            return "Please include an @ sign"

    def validatate_user_username(self, username):
        if not username:
            return "Username cannot be field"
        if not isinstance(username, str):
            return "Please username should be a string"

    def validate_user_first_name(self, first_name):
        if not first_name:
            return "First_name missing"

        if not isinstance(first_name, str):
            return "Please first_name should be a string"

    def validate_user_last_name(self, last_name):
        if not last_name:
            return "Last_name missing"

        if not isinstance(last_name, str):
            return "Please last_name should be a string"

    def validate_user_other_name(self, other_name):
        if not other_name:
            return "Last_name missing"

        if not isinstance(other_name, str):
            return "Please last_name should be a string"
