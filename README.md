# project-b-20
project-b-20 created by GitHub Classroom

## Setting up dev environment ##

* Install virtualenv
`pip3 install virtualenv`

* Run in root directory of the project
`virtualenv -p python3 env`

* To activate the virtual environment, run
`source env/bin/activate`

* The environment should activate, with a "(env)" in front of the PS1 (shell prompt)

* `pip3 install -r requirements.txt` will install the required packages

* When models are updated, make migrations with
`python3 manage.py makemigrations`

* To populate the database, run migrations with
`python3 manage.py migrate`

* To run the development server, run
`python3 manage.py runserver`

## Configuration ##

* Use `pip3 freeze > requirements.txt` to maintain requirements
