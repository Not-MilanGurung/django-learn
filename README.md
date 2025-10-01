# my-games-list
Personal project to record the games like [HowLongToBeat](https://howlongtobeat.com/). It is made up of these apps:

* listing

## Initial setup
1) You need to first create a venv envrionment and install the `requirement.txt`

2) Create a '.env' with
    ```env
    SECRET_KEY='your_security_key' // key for django and jwt; use a key generator

    DATABASE_ENGINE='your database engine' // for example 'django.db.backends.postgresql'
    DATABASE_NAME='name_of_your_database'
    DATABASE_USER='name_of_user'
    DATABASE_PASSWORD='password_of_user'
    DATABASE_HOST='database_host' // for example 'localhost'
    DATABASE_PORT= // port of the database like 5432 for postgres default

    // Token lifetime in int; modify to fit your need
    // Modify config.py if you want to use other units, not just minutes and days
    JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES = 5
    JWT_REFRESH_TOKEN_LIFETIME_IN_DAYS = 1
    JWT_SLIDING_TOKEN_LIFETIME_IN_MINUTES = 5
    JWT_SLIDING_TOKEN_REFRESH_LIFETIME_IN_DAYS = 1
    ``` 

3) Make migrations: `python myGamesList/manage.py makemigrations listing`

4) Run the initial migration: `python myGamesList/manage.py migrate`

5) Run the server `python myGamesList/manage.py runserver` 


