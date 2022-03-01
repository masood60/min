from django.urls import path
from foods import views

urlpatterns = [
    path("",views.list_foot,name='index'),
]

    