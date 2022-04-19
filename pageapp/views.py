from django.shortcuts import render
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "home.html"

"""def index(request):
    return render (request,'home.html')"""
    
class AboutpageView(TemplateView):
    template_name="about.html"


