from django.db import models

# Create your models here.
from django.db import models

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
      
    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)


    def __str__(self):
        return self.author


class country(models.Model):
    cname=models.CharField(primary_key=True,max_length=100) 

    def __str__(self):
        return self.cname
class capital(models.Model):
    cname=models.ForeignKey(Topic,on_delete=models.CASCADE)               
