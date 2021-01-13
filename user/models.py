from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    mobile_number = models.BigIntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    user_image = models.ImageField(null=True, blank=True)

    @property
    def ImageURL(self):
        try:
            url = self.user_image.url
        except ValueError:
            url = ''
        return url