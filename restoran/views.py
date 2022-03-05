from django.views.generic import TemplateView
from django.shortcuts import render

class about(TemplateView):
    template_name = "about.html"

class index(TemplateView):
    template_name = "index.html"
