# Roommate Connector - Team B-20 
Roommate Connector's matching algorithm helps to find you compatible roommates based on a variety of factors. 

## Usage ##
* In chat rooms, you can click on a person's profile above the chat to visit their profile page.
* On the map, right click and select to either set the pin somewhere or to change the radius.
* You can remove all of your matches by deselecting the match enabled option in your profile. You will be removed from everyone else's matches as well.
* Find your profile in the top right of the page!
* Roommate matches are sorted by their percent compatibility with you.
* Setting your min match percentage changes the bottom threshold for matches - a higher number means you'll see fewer matches.

## Development ##

* Install virtualenv
`pip3 install virtualenv`

* Run in root directory of the project
`virtualenv -p python3 env`

* To activate the virtual environment, run
`source env/bin/activate`

* The environment should activate, with a "(env)" in front of the PS1 (shell prompt)

* `pip3 install -r requirements.txt` will install the required packages. If this gives an error on Mac, comment out `django-heroku` and `psycopg2-binary`

* When models are updated, make migrations with
`python3 manage.py makemigrations`

* To populate the database, run migrations with
`python3 manage.py migrate`

* To run the development server, run
`python3 manage.py runserver`

* To create a superuser, run
`python3 manage.py createsuperuser`

## Maintaining Dependencies ##
* Use `pip3 freeze > requirements.txt` to maintain requirements, if adding or removing dependencies
* Make sure that `pkg-resources==0.0.0` is not present in `requirements.txt`
