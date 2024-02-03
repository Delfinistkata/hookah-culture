"""
Custom storage configurations for
handling static and media files on AWS S3.
This module defines two custom storage classes,
`StaticStorage` and `MediaStorage`, both derived
from `S3Boto3Storage`. These classes are used
to set the storage locations for static and media
files on AWS S3 as specified in the `STATICFILES_LOCATION`
and `MEDIAFILES_LOCATION` settings, respectively.
"""
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Custom storage class for handling static files on AWS S3.
    Uses S3Boto3Storage as the base class and sets the location
    for storing static files to the value specified in the
    STATICFILES_LOCATION setting.
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    Custom storage class for handling media files on AWS S3.
    Uses S3Boto3Storage as the base class and sets the location
    for storing media files to the value specified in the
    MEDIAFILES_LOCATION setting.
    """
    location = settings.MEDIAFILES_LOCATION
