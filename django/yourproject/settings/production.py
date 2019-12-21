# Parse database configuration from $DATABASE_URL
import dj_database_url
from os import environ

from .base import *

ALLOWED_HOSTS = ['ec2-18-223-158-21.us-east-2.compute.amazonaws.com/','ec2-3-135-198-122.us-east-2.compute.amazonaws.com']

DATABASES = {
    'default': dj_database_url.config()
}

STATIC_ROOT = environ['STATIC_ROOT']
