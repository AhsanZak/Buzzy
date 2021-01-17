from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
# Create your models here.
from thumbnails.fields import ImageField


class ImageDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, null=True)
    category = models.TextField(null=True)
    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    # image = ImageField(null=True, blank=True, resize_source_to="small")
    image_thumbnail = ImageSpecField(source='image', format='JPEG', options={'quality': 8})
    approval = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except ValueError:
            url = ''
        return url
