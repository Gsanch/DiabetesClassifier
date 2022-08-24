import re
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import testresult
from .forms import testform
from .serializers import testresultSerializers
import pickle
from django.views.decorators.csrf import csrf_exempt

with open('trained_model', 'rb') as trained_model:
    clf= pickle.load(trained_model)

class Adressview (ModelViewSet):
    serializer_class = testresultSerializers
    queryset = testresult.objects.all()
# Create your views here.
@csrf_exempt
def mydata(request):
    # print("Hello")
    # print(request)
    return HttpResponse(request)
    if request.method=='POST':
      
        Age=request.POST['Age']
        insulin=request.POST['insulin']
        BMI=request.POST['BMI']
        Bloodpressure=request.POST['Bloodpressure']
        retinopathy=request.POST['retinopathy']
        # eyedamage=request.POST['eye damage']
        Glucose=request.POST['Glucose']
        # phyicalhealth=request.POST['phyical health']
    
    sample=[[Age,insulin,BMI,Bloodpressure,retinopathy,Glucose]]
    result=clf.predict(sample)
    print(result)
    
    
 
    
