from rest_framework.routers import DefaultRouter
from .views import Adressview
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register('apidata', Adressview)

urlpatterns = [
# path('test/', views.testing, name='testing'),
path('api/', include(router.urls)),
path('form/', views.mydata, name='testing')
]
