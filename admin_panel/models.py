from django.db import models


# Create your models here.

class ImageDetail(models.Model):
    product_name = models.CharField(max_length=100, null=True)
    product_description = models.TextField(null=True)
    product_price = models.IntegerField(null=True)
    product_image = models.ImageField(null=True, blank=True)

    @property
    def ImageURL(self):
        try:
            url = self.product_image.url
        except ValueError:
            url = ''
        return url
