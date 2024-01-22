from django.db import models
 
class Person(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    saved = models.DateTimeField(auto_now=True)