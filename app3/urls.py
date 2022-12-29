from django.urls import path
from app3.views import*
app_name='name3'

urlpatterns=[
    path('bts/',bts,name='bts'),
]