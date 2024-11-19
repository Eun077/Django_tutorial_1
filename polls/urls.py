from django.contrib import admin
from django.urls import path
#from polls import views  path('', views.index)
#from . import views    path('', views.index)
#from polls.views import index, index1, index2  path('', index)
from .views import index, index1, index2
urlpatterns = [
    path('', index),
    path('django/', index1),
    path('test/', index2)
]