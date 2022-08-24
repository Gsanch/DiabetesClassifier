
from unittest.util import _MAX_LENGTH
from django import forms

class testform(forms.Form):

    
    
    Age=forms.IntegerField()
    insulin=forms.CharField(max_length=15)
    BMI=forms.IntegerField()
    Bloodpressure=forms.CharField(max_length=15)
    # eyedamage=forms.CharField(max_length=15)
    Glucose=forms.CharField(max_length=15)
    retinopathy=forms.CharField(max_length=15)
    # phyicalhealth=forms.IntegerField()
    

