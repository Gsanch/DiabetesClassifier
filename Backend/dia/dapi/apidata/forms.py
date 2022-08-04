
from unittest.util import _MAX_LENGTH
from django import forms

class testform(forms.Form):

    

    firstname=forms.CharField(max_length=15)
    lastname=forms.CharField(max_length=15)
    age=forms.IntegerField()
    phyicalhealth=forms.CharField(max_length=15)
    insulin=forms.CharField(max_length=15)
    BMI=forms.IntegerField()
    Bloodpressure=forms.CharField(max_length=15)
    eyedamage=forms.CharField(max_length=15)
    Glucose=forms.CharField(max_length=15)
    retinopathy=forms.CharField(max_length=15)
    
    

