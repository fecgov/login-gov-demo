from django.db import models
from django.contrib.auth.models import User

class FECFileUser(models.Model):
    """
    Add UUID from login.gov to default User model
    https://developers.login.gov/attributes/
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=36)
    # TODO: may want `all_emails`, `phone`
