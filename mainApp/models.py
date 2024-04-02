from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = RichTextField()
    conclusion = models.TextField()
    date = models.DateField(auto_now=False)
    image = models.ImageField(upload_to="uploads")
    
    def __str__(self):
        return str(self.id)+" "+self.title
    
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = RichTextField()
    conclusion = models.TextField()
    date = models.DateField(auto_now=False)
    image = models.ImageField(upload_to="uploads")
    
    def __str__(self):
        return str(self.id)+" "+self.title
    
class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="uploads")
    facebook_link = models.CharField(max_length=1000)
    twitter_link = models.CharField(max_length=1000)
    instagram_link = models.CharField(max_length=1000)
    
    def __str__(self):
        return str(self.id)+" "+self.name