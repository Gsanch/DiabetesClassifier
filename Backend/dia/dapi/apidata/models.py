
from msilib.schema import InstallUISequence
from django.db import models


class testresult(models.Model):

    

    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    age=models.IntegerField(default=0)
    insulin=models.CharField(max_length=15)
    
   

   

    def __str__(self):
        return self.firstname, self.lastname,