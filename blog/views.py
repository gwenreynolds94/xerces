from django.shortcuts import render

# Create your views here.
def blog_index(request):
    return render(request, template_name="blog/index.html")