from django.db import models

# Create your models here.
class Student(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=64)
    age=models.IntegerField()
    gender=models.CharField(max_length=7)

    class Meta:
        ordering=['-no']

    def __str__(self):
        return self.name    
