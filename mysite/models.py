from django.db import models

# Create your models here.


class Designation(models.Model):
        DesignationName=models.CharField(max_length=30);
        Status = models.CharField(max_length=30);