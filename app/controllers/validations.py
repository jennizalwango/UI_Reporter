
class Validators:

    def validatate_user_email(self, email):
        if not email:
            return "Email field cannot be left out"

        if not "@" in email:
            return "Please include an @ sign"

        if type(email) != str:
            return "Email should be a string"
        email = (email).strip()


    def validatate_user_username(self, username):
        if not username:
            return "Username cannot be a missing field"

        if not isinstance(username, str):
            return "Please username should be a string"
        username = (username).strip()

    def validate_user_fields_missing(self, first_name, last_name, other_name):
        if not first_name:
            return "First_name missing"
        
        if not last_name:
            return "Last_name missing"

        if not other_name:
            return "Other_name missing"   

    def validate_user_fields_are_strings(self, first_name, last_name, other_name):
        if not isinstance(first_name, str):
            return "Please first_name should be a string"
        first_name = (first_name).strip()

        if not isinstance(last_name, str):
            return "Please last_name should be a string"
        last_name = (last_name).strip()

        if not isinstance(other_name, str):
            return "Please other_name should be a string"
        other_name = (other_name).strip()
