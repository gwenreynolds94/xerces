from django.urls import path
from . import views

urlpatterns = [
    path('', views.sessfun, name='sessfun')
]