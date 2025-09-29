import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

SECRET_KEY= os.getenv('SECRET_KEY')
POSTGRES_DATABASE=os.getenv('POSTGRES_DATABASE')
POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
JWT_ACCESS_TOKEN_LIFETIME = timedelta(minutes=int(os.getenv('JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES')))
JWT_REFRESH_TOKEN_LIFETIME = timedelta(days=int(os.getenv('JWT_REFRESH_TOKEN_LIFETIME_IN_DAYS')))
JWT_SLIDING_TOKEN_LIFETIME = timedelta(minutes=int(os.getenv('JWT_SLIDING_TOKEN_LIFETIME_IN_MINUTES')))
JWT_SLIDING_TOKEN_REFRESH_LIFETIME = timedelta(days=int(os.getenv('JWT_SLIDING_TOKEN_REFRESH_LIFETIME_IN_DAYS')))