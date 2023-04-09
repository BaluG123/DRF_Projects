from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    eage=models.IntegerField()
    eaddr=models.CharField(max_length=126)
    epic=models.ImageField(null=True,blank=True,upload_to='images/')

    class Meta:
        ordering=['eno']

    def __str__(self):
        return self.ename    