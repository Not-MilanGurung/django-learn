# django-learn
Learning Django

# Initial setup
1) You need to first create a venv envrionment and install the `requirement.txt`

2) Create a file `myGamesList/myGamesList/securityKeys.py` with const `SECURITY_KEY` with a key(String value) generated for django (use a website online to generate)

3) Create a postgres database and enter the details in the `myGamesList/myGamesList/settings.py` under `DATABASE` field (user, password, name of database, port, etc)

4) Run the initial migration: `python myGamesList/manage.py migrate`

5) Run the server `python myGamesList/manage.py runserver` 

> The **test** project is setup with sqlite so you can skip step 2 & 3 
# Projects and their apps

## 1) myGamesList
Personal project to record the games like [HowLongToBeat](https://howlongtobeat.com/)

* listing

## 2) test
Project made following most of [w3school's Django tutorial](https://www.w3schools.com/django/index.php)
	
* simapple
