from django.db import models


class Website(models.Model):
    url = models.URLField()
    meta_description = models.CharField(max_length=1500)
    meta_title = models.CharField(max_length=250)
