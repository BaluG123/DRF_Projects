from django.db import models

# Create your models here.
class Employee(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=64)
    age=models.IntegerField()
    gender=models.CharField(max_length=6)

    class Meta:
        ordering=['-no']

    def __str__(self):
        return self.name    