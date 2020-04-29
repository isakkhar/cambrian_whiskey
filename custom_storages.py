from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
  location = settings.STATICFILES_LOCATION
  
# we can add another class to deal with media

class MediaStorage(S3Boto3Storage):
  location = settings.MEDIAFILES_LOCATION


