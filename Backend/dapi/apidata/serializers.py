# from dataclasses import fields
# from rest_framework.serializers import ModelSerializer
# from .models import testresult

# class ApiSer (ModelSerializer):
#     class Meta :
#         model = testresult
#         fields = '__all__'
# from dataclasses import fields
# from pyexpat import model

from rest_framework import serializers
from .models import testresult

class testresultSerializers(serializers.ModelSerializer):
    class Meta:
        model = testresult
        fields = '__all__'