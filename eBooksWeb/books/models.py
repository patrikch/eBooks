from django.db import models
from django.db.models import Q

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
    keys = models.ManyToManyField(Key)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name + " (" + self.authors + ")"

class BookRep:
    def find(self,spojka=None,name=None,authors=None,publisher=None,location=None,
         pubYear=None):

        q1,q2,q3,q4,q5 = None,None,None,None,None
        if name != None and len(name) > 0:
            q1 = Q(name__icontains=name)
        if authors != None and len(authors) > 0:
            q2 = Q(authors__icontains=authors)
        if publisher != None and len(publisher) > 0:
            q3 = Q(publisher__icontains=publisher)
        #if location != None:
        #    q4 = Q(location__icontains=location)
        if pubYear != None:
            q5 = Q(pubYear__iexact=int(pubYear))
            
        first = None
        for qx in [q1,q2,q3,q4,q5]:
            if first == None:
                if qx != None:
                    first = qx
            else:
                if qx != None:
                    if spojka == "AND":
                        first = first & qx
                    else:
                        first = first | qx
                    
        print(first)
        result = []
        try:
            result = Book.objects.filter(first)
        except:
            pass
        print(len(result))
        return result
    


        
        
        
            
            
    
