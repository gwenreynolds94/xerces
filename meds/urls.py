from django.urls import path
from . import views

app_name = 'meds'
urlpatterns = [
<<<<<<< HEAD
    path('', views.IndexView, name='index'),
=======
    path('', views.IndexView.as_view(), name='index'),
>>>>>>> 1da8358ea4f1ce528f420afbb7c53e14dbc41e33
    path('update-medication-list/', views.UpdateMedicationList.as_view(), name='update-medication-list')
]
