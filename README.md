[![Build Status](https://travis-ci.org/jennizalwango/UI_Reporter.svg?branch=ft-api-endpoints)](https://travis-ci.org/jennizalwango/UI_Reporter)  [![Maintainability](https://api.codeclimate.com/v1/badges/01e28c736b9d02cdb7d8/maintainability)](https://codeclimate.com/github/jennizalwango/UI_Reporter/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/jennizalwango/UI_Reporter/badge.svg?branch=ft-api-endpoints)](https://coveralls.io/github/jennizalwango/UI_Reporter?branch=ft-api-endpoints)

#  Section for UI_Reporter:
A self journalism report system which lets a user to create red flags and interventions .Report on differnt cases that are affecting them and can call for hlp from government.

## Description 

This is the User Interface of the project, User creates account. The user can also just login if account is created already.
User is able to create red flags or interventions depending on what the issue is.

The user is able see the number of red flags created and number of interventons created by other user.
The admin is the one who  updates status of the user and delete what they think needs to be deleted.

The user is able to know the number of red flags and interventions resolved , rejected ,restricted and the ones under investigation.

There are different pages a can navigate around with At the start a user is exepected to sign up in order to go on with all they want to to.

From sigining up the user is free to navigate through the applictaion where they also create their own incidents , see how many are created already.

## Project Folders;
The UI for the web application has been mainly built with Html and Css and some lines of javascript.
 The files have been put in `Folders` according to what should be where and why.


  For all the `html` has been used in the making of the project can be found in the ` Html Folder`

  Some of the html files in the html folder are;

  `veiw_record.html` A user is able to see the created incident by other users 

  `create html` A user is able to create incident whether there interventions or redflags.

  `login.html`  A user is able to log in to the system.

  For all the `css` that has been used in the making of the project it can be found in the `Css Folder`

  There is also an images folder 

  This is the link to the gh-pages
  https://github.com/jennizalwango/UI_Reporter/tree/gh-pages

#  Section for the End Points:
This is an online application that let users nagavigate through the application.
I-Reporter is a platform where people can report incidents of corruption.
Users can do the following;
Create a ​red-flag​​ record, Get all ​red-flag​​ records, Get a specific ​red-flag​​ record Edit a specific ​red-flag​​ record and also Delete a ​red-flag​​ record

A self journalism report system which lets a user to create red flags and interventions .Report on different incidents of corruption that are affecting them and can call for help from government.

This is the User Interface of the project, User creates account. The user can also just login if account is created already.
User is able to create red flags or interventions depending on what the issue is.

The user is able see the number of red flags created and number of interventons created by other user.
The admin is the one who  updates status of the user and delete what they think needs to be deleted.

The user is a to know the number of red flags and interventions resolved , rejected ,restricted and the ones under investigation.

## Prerequisties
Inorder  to run this application you need the following;
you need to have [python3](https://www.python.org/downloads/)  installed on your machine.

You need to have [flask](http://flask.pocoo.org/docs/1.0/installation/) installed on your machine.

## Installing 

##You have to install a virutualenvirnoment, 
 `pip3 install virtualenv`.


##Create the virtual envirnoment
 `virtualenv ireporter`.


##Activate your virtualenv to start working.
 `source ireporter/bin/activate`.

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
