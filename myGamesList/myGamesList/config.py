import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

SECRET_KEY= os.getenv('SECRET_KEY')

DATABASE_ENGINE=os.getenv('DATABASE_ENGINE')
DATABASE_NAME=os.getenv('DATABASE_NAME')
DATABASE_USER=os.getenv('DATABASE_USER')
DATABASE_PASSWORD=os.getenv('DATABASE_PASSWORD')
DATABASE_HOST=os.getenv('DATABASE_HOST')
DATABASE_PORT=os.getenv('DATABASE_PORT')

JWT_ACCESS_TOKEN_LIFETIME = timedelta(minutes=int(os.getenv('JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES')))
JWT_REFRESH_TOKEN_LIFETIME = timedelta(days=int(os.getenv('JWT_REFRESH_TOKEN_LIFETIME_IN_DAYS')))
JWT_SLIDING_TOKEN_LIFETIME = timedelta(minutes=int(os.getenv('JWT_SLIDING_TOKEN_LIFETIME_IN_MINUTES')))
JWT_SLIDING_TOKEN_REFRESH_LIFETIME = timedelta(days=int(os.getenv('JWT_SLIDING_TOKEN_REFRESH_LIFETIME_IN_DAYS')))