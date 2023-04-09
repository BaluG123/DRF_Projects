from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    eage=models.IntegerField()
    eaddr=models.CharField(max_length=64)

    class Meta:
        ordering=['eno']

    def __str__(self):
        return self.ename     