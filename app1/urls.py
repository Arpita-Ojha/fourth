from django.urls import path
from app1.views import*

app_name='name1'

urlpatterns=[
    path('one/',one,name='one'),
    path('two/',two,name='two'),
    path('v/',v,name='v'),
]