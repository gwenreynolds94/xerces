from django.shortcuts import render

# Create your views here.
def home_index(request):
    return render(request, template_name="home/index.html")

def about_page(request):
    return render(request, template_name="home/about.html")