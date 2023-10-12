from django.urls import path
from maps.views import *

urlpatterns = [
    path('',index,name='index')
]