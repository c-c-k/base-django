"""Authentication overrides and extensions

Placeholder module for extending and overriding Django's builtin
authentication models.

https://docs.djangoproject.com/en/4.1/topics/auth/default/#using-the-django-authentication-system
https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django-contrib-auth
"""
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    """User overrides and extensions

    A placeholder for overriding the Django builtin User model.
    AUTH_USER_MODEL should be set to this model in settings.py
    for this user model to work properly.

    Django's default User model info:
    https://docs.djangoproject.com/en/4.1/topics/auth/default/#user-objects
    https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#user-model
    Django's customizing and extending the User model info:
    https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model
    https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-the-existing-user-model
    """
    pass

    class Meta(auth_models.AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
