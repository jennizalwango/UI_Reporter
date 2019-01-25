import re

class Validators:
    def validate_user_input(self, username, first_name, last_name, other_name, email, password):
        if not username or username.isspace():
            return "Username field can not be left empty."

        elif not first_name or first_name.isspace():
            return "Frist name can not be left empty."

        elif not last_name or first_name.isspace():
            return "Last name can not be left empty."

        elif not other_name or other_name.isspace():
            return "Other name can not be left empty."

        elif not email or email.isspace():
            return "Email field can not be left empty."

        elif not re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)" , email):
            return "Enter a valid email address."

        elif not password or password.isspace():
            return "Password field can not be left empty."

        elif len(password) < 6:
            return "Password must be of 6 charaters"



    def validate_create_input(self,created_by, incident_type, location, phone_number, status, images,       videos, comment):  
        if not created_by or created_by.isspace():
            return "Please fill the created_by field"

        if not incident_type or incident_type.isspace():
            return "Please fill in the incident_type field"

        if  not location or location.isspace():
            return "Please fill the location field"
        
        if  not phone_number or phone_number.isspace():
            return "Plesae provide the phone_number"
            
        if  not status  or status.isspace():
            return "Please fill the status field"
                
        if  not images or images.isspace():
            return "Please provide some images"

        if  not videos  or videos.isspace():
            return "Please provide some videos"

        if  not comment or comment.isspace:
            return "Please leave a comment"

        if not type(phone_number) == int:
            return "Phone number must be an integer"  
            
    def validate_login_input(self, username, password):
        if not password or password.isspace():
            return "Password field can not be left empty."

        if not username or username.isspace():
            return "Username field can not be left empty."


