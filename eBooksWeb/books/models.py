from django.db import models

class Key(models.Model):
    key = models.CharField(max_length=20)
    parent = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.key

class Location(models.Model):
    dvd = models.CharField(max_length=10)

    def __str__(self):
        return self.dvd

class Book(models.Model):
    ebookfilename = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    authors = models.CharField(max_length=100,blank=True)
    publisher = models.CharField(max_length=50,blank=True)
    format = models.CharField(max_length=5)
    pubYear = models.IntegerField(null=True,blank=True)
    keys = models.ManyToManyField(Keys)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name + " (" + self.authors + ")"
    
