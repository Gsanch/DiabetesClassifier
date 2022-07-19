
from unittest.util import _MAX_LENGTH
from django import forms

class testform(forms.Form):
    firstname=forms.CharField(max_length=15)
    lastname=forms.CharField(max_length=15)
    age=forms.IntegerField()
    
    

