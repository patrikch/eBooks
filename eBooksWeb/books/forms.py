from django import forms
from books import models

SPOJKA_CHOICES = (
    ("AND","and"),
    ("OR","or"),
    )

def get_locations():
        lst = []
        for l in models.Location.objects.all():
            lst.append((l.id,l.dvd))
        return lst

class SearchForm(forms.Form):
    spojka = forms.ChoiceField(label="Spojka",widget=forms.RadioSelect,
                               choices=SPOJKA_CHOICES,required=True)
    name = forms.CharField(label="Name",max_length=100,required=False)
    authors = forms.CharField(label="Authors",max_length=100,required=False)
    publisher = forms.CharField(label="Publisher",max_length=50,required=False)
    location = forms.ChoiceField(label="Location",choices=get_locations(),required=False)
    pubYear = forms.IntegerField(label="Pub.year",required=False)
    sort = forms.CharField(widget=forms.HiddenInput,required=False)
    

    
    
    
    
