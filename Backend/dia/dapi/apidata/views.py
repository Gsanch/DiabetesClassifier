from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import testresult
from .forms import testform
from .serializers import testresultSerializers

class Adressview (ModelViewSet):
    serializer_class = testresultSerializers
    queryset = testresult.objects.all()
# Create your views here.

def mydata(request):
    if request.method=='POST':
        form=testform(request.POST)
        #validation
        firstname=form.cleaned_data['firstname']
        lastname=form.cleaned_data['lastname']
        age=form.cleaned_data['age']
        phyicalhealth=form.cleaned_data['phyicalhealth']
        insulin=form.cleaned_data['insulin']
        BMI=form.cleaned_data['BMI']
        Bloodpressure=form.cleaned_data['Bloodpressure']
        Glucose=form.cleaned_data['glucose']
        eyedamage=form.cleaned_data['eyedamage']
        retinopathy=form.cleaned_data['retinopathy']

       
        
        
    form=testform()
    return render(request, 'testing.html', {'form':form})

