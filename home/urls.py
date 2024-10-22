from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_index, name='home-page'),
    path('about/', views.about_page, name='about-page'),
]
