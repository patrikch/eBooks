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
         pubYear=None,sort=None):

        q1,q2,q3,q4,q5 = None,None,None,None,None
        if name != None and len(name) > 0:
            q1 = Q(name__icontains=name)
        if authors != None and len(authors) > 0:
            q2 = Q(authors__icontains=authors)
        if publisher != None and len(publisher) > 0:
            q3 = Q(publisher__icontains=publisher)
        if location != None:
            q4 = Q(location__id__iexact=location)
        if pubYear != None:
            q5 = Q(pubYear__iexact=int(pubYear))
            
        q = Q()
        for qx in [q1,q2,q3,q4,q5]:
            if qx != None:
                if spojka == "AND":
                    q = q & qx
                else:
                    q = q | qx

        print(q)
        sortExpr = self.sort(sort)
        print(sortExpr)
        result = []
        try:
            if sortExpr == None:
                result = Book.objects.filter(q)
            else:
                result = Book.objects.filter(q).order_by(sortExpr)
        except:
            pass
        print(len(result))
        return result

    def sort(self,sort):        
        #Neni sortovaci vyraz
        if sort == None or len(sort) == 0:
            return None
        
        tmp = sort.lower()
        prefix = ""
        #nedava se +name,ale jen name anebo -name
        if sort.startswith("+") or sort.startswith("-"):
            tmp = sort[1:].lower()
            if sort.startswith("-"):
                prefix = sort[0:1]
        #v sort vyrazu neni povoleny sloupec        
        if tmp not in ("name","authors","publisher","format","pubyear","location"):
            return None

        if tmp == "location":
            tmp = "location__dvd"
        if tmp == "pubyear":
            tmp = "pubYear"

        return prefix + tmp 


        
        
        
            
            
    
