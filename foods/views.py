from django.views.generic import TemplateView
from django.shortcuts import render
from foods.models import food

# Create your views here.

def list_foot(request):
    query=food.objects.all()
    context={
        "object":query
    }
    return render(request,"index.html",context)
    

