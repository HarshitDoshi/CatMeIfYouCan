from django.db import models


class CatPicture(models.Model):
    title = models.CharField(max_length=128, blank=True, null=False)
    description = models.TextField(blank=True, null=False)
    image = models.ImageField(upload_to="CatPictures")
