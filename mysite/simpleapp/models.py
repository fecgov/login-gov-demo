from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Add UUID from login.gov to default User model
    https://developers.login.gov/attributes/
    https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    """
    uuid = models.CharField(max_length=36)
    # TODO: may want `all_emails`, `phone`
    # Allow first and last names to be blank
    first_name= models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)
