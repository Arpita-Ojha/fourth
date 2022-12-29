from django.urls import path
from app2.views import*
app_name='name2'

urlpatterns=[
    path('one/',one,name='one'),
    path('jimin/',jimin,name='jimin'),
]
