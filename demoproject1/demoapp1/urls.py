
from django.urls import path

from demoapp1 import views

urlpatterns = [

    path("",views.demo,name="demo"),

]