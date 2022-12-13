from django.db import models

# Create your models here.
# We create all our databases here
class Feature(models.Model):
  name =  models.CharField(max_length=100)
  details = models.CharField(max_length=500)
  is_true: bool