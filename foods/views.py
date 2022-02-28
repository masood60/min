from django.views.generic import TemplateView
from django.shortcuts import render
from foods.models import food

# Create your views here.
def list_food(request):
    query=food.objects.all()
    context={
        'object':query
    }
    return render(request,'index.html',context)
def detail_food(request,ID):
    query=food.objects.get(id=ID)
    context={
        'object':query
    }
    return render(request,'foods/detail_food.html',context)

class about(TemplateView):
    template_name = "about.html"
