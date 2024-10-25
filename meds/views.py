from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView
from .models import Medication

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "meds/index.html"

# Create your views here.
class UpdateMedicationList(LoginRequiredMixin, View):
    def post(self, request):
        from bs4 import BeautifulSoup
        import requests
        
        az = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        names = []
        for alpha in az:
            r = requests.get(f"http://rxlist.com/drugs/alpha_{alpha}.htm")
            soup = BeautifulSoup(r.text, features="html.parser")
            div = soup.find_all("div", class_="AZ_results")[0]
            for li in div.find_all("li"):
                names.append(li.text)
        
        Medication.objects.all().delete()
        for name in names:
            Medication(name=name).save()
        
        return redirect("meds/index.html")