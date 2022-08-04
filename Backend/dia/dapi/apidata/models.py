
from msilib.schema import InstallUISequence
from django.db import models


class testresult(models.Model):



    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    age=models.IntegerField(default=0)
    phyicalhealth=models.CharField(max_length=15)
    insulin=models.CharField(max_length=15)
    BMI=models.IntegerField(default=0)
    Bloodpressure=models.CharField(max_length=15)
    eyedamage=models.CharField(max_length=15)
    Glucose=models.CharField(max_length=15)
    retinopathy=models.CharField(max_length=15)
    
    
   

   

    def __str__(self):
        return self.firstname, self.lastname,