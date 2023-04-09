from django.db import models

# Create your models here.
class Employee(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=64)
    age=models.IntegerField()
    addr=models.CharField(max_length=128)

    class Meta:
        ordering=['-no']

    def __str__(self):
        return self.name    
