[![Build Status](https://travis-ci.org/jennizalwango/UI_Reporter.svg?branch=ft-api-endpoints)](https://travis-ci.org/jennizalwango/UI_Reporter)

# UI_Reporter
## SECTION A:
## UI.
A self journalism report system which lets a user to create red flags and interventions .Report on different incidents of corruption that are affecting them and can call for help from government.

This is the User Interface of the project, User creates account. The user can also just login if account is created already.
User is able to create red flags or interventions depending on what the issue is.

The user is able see the number of red flags created and number of interventons created by other user.
The admin is the one who  updates status of the user and delete what they think needs to be deleted.

The user is a to know the number of red flags and interventions resolved , rejected ,restricted and the ones under investigation.


## SECTION B :
## API ENDPOINTS.
This is an online application that let users nagavigate through the application.
I-Reporter is a platform where people can report incidents of corruption.
Users can do the following;
Create a ​red-flag​​ record, Get all ​red-flag​​ records, Get a specific ​red-flag​​ record Edit a specific ​red-flag​​ record and also Delete a ​red-flag​​ record


## Prerequisties
Inorder  to run this application you need the following;
you need to have [python3](https://www.python.org/downloads/)  installed on your machine.

You need to have [flask](http://flask.pocoo.org/docs/1.0/installation/) installed on your machine.

## Installing 

####You have to install a virutualenvirnoment, 
 `pip3 install virtualenv`

####Create the virtual envirnoment
 `virtualenv ireporter`

####Activate your virtualenv to start working.
 `source ireporter/bin/activate`

Install the app dependencies,these are found in the `requirements.txt`

Configure the environment variables, ie `IREPORTER_ENV` and the `SECRET_KEY`.

The application is bulit with a python flamework called [Flask](http://flask.pocoo.org/).
Go on and install pylint to help you run the tests of the application
###To run the tests:
  `pytest`  or
  `py.test --cov`  and this will show you the coverage of the tests locally

Install all application requirements from the requirements files found in the root folder
 `pip install -r requirements`
All done! Now,start your server by running  `python run.py`.

## Functionality
-Create a red-flag record
-Get all red flag records
-Get specific red flag record
-Edit a red-flag's location
-Edit a red-flag's comment
-Delete red flag record

## Supported Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   |/api/v1/register/ |Create User|
| POST   |/api/v1/login/ |Log in User|
| POST   |/api/v1/incident/ |Create red flag or intervention|
| GET    |/api/v1/incident/all|Get all created incidents|
| GET    |/api/v1/incident/<incident_id>/|Get specific red flag|
| PATCH  |/api/v1/incident/<incident_id>/location/|Edit red flag location|
| PATCH  |/api/v1/incident/<incident_id>/comment/|Edit red flag comment|
| DELETE |/api/v1/red-flags/<incident_id>/|Delete red flag|
