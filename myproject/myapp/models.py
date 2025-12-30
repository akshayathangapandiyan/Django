from django.db import models

# Create your models here.
"""class employee(models.Model):
    name = models.CharField(max_length=100)"""
    
"""#class student(models.Model):
    #name = models.CharField(max_length=100)
    #age = models.IntegerField()
    #mark = models.IntegerField()
    #subject = models.CharField(max_length=200)"""


class jaishaa(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mark = models.IntegerField()
    sub = models.CharField(max_length=200)

class student_ser(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.CharField(max_length=100)


    

    #signals:


    class student_signals(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()


    def __str__(self):
        return self.name