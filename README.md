# AudRate

#### 19 October 2019
By Audrey Njiraini

## Overall Project Description
This is an application that allows a user to post a project he/she has created and get it reviewed by his/her peers. A project can be rated based on three different criteria:
<ol>
    <li>Design</li>
    <li>Usability</li>
    <li>Content</li>
</ol>
These criteria can be reviewed on a scale of 1-10 and the average score is taken.

## User stories
<ol>
    <li>A user can view posted projects and their details.</li>
    <li>A user can post a project to be rated/reviewed. </li>
    <li>A user can rate/review other users' projects.</li>
    <li>A user can search for projects .</li>
    <li>A user can view projects' overall score.</li>
    <li>A user can view their profile page.</li>

</ol>


## Setup/Installation Requirements
* Python version 3.6
* pip
* Django version 1.11.23
* Django-bootstrap3
* Heroku
* Gunicorn
* Internet connection

## Installation Process
<ol>
    <li>Navigate to https://github.com/audreynjiraini/awwwards .</li>
    <li>Clone the project.</li>
    ``` git clone https://github.com/audreynjiraini/awwwards.git ```
    <li>Navigate to the project folder in your terminal.</li>
    <li>Create a virtual environment</li>
    ``` python3.6 -m venv virtual ```
    <li>Activate the virtual environment</li>
    ``` source virtual/bin/activate ```
    <li>Install the requirements</li>
    ``` pip install -r requirements.txt ```
    <li>In project/settings.py file, ensure that DEBUG = True.</li>
    <li>Run the server</li>
    ``` python3.6 manage.py runserver ```
</ol>

## Known Bugs
No known bugs.

## Contact Information
If you need clarification on any aspect, feel free to reach me via email at audreynjiraini@gmail.com

### License
MIT License [MIT](license.txt)
Copyright (c) 2019 Audrey Njiraini
