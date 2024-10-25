from django.urls import path
from . import views

app_name = 'meds'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('update-medication-list/', views.UpdateMedicationList.as_view(), name='update-medication-list')
]
