from django.conf.urls import url
from . import views

#Redirecting to views.py File
urlpatterns=[
    url(r'^$',views.details),
]