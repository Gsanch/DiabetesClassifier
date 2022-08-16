import re
from django.template import RequestContext
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import testresult
from .forms import testform
from .serializers import testresultSerializers
import pickle
from django.views.decorators.csrf import csrf_exempt

class Adressview (ModelViewSet):
    serializer_class = testresultSerializers
    queryset = testresult.objects.all()
# Create your views here.
@csrf_exempt
def mydata(request):
    print("Hello")
    print(request)
    if request.method=='POST':
        form=testform(request.POST)
        #validation
        firstname=form.cleaned_data['firstname']
        lastname=form.cleaned_data['lastname']
        age=form.cleaned_data['age']
        insulin=form.cleaned_data['insulin']
        BMI=form.cleaned_data['BMI']
        Bloodpressure=form.cleaned_data['Bloodpressure']
        # Glucose=form.cleaned_data['glucose']
        # eyedamage=form.cleaned_data['eyedamage']
        retinopathy=form.cleaned_data['retinopathy'] 

        with open('trained_model', 'rb') as trained_model:
            clf= pickle.load(trained_model)

    
 
    

       
        
        
    form=testform()
    return render(request, 'testing.html', {'form':form})
    return render_to_response('fileupload/upload.html', {'testing': c['UploadFiletesting']},  RequestContext(request))

