from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Article(models.Model):
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=50,default='')
    pub_time = models.DateTimeField()
    new_type = models.CharField(max_length=20,default='')
    content = HTMLField()

class College(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField()