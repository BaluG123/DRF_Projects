from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=124)
    eage=models.IntegerField()
    egender=models.CharField(max_length=6)

    class Meta:
        ordering=['eno']

    def __str__(self):
        return self.ename    