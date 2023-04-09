from django.db import models

# Create your models here.
class Student(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=124)
    age=models.IntegerField()
    gender=models.CharField(max_length=6)
    gmail=models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        ordering=['no']    