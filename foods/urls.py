from django.urls import path
from foods import views

urlpatterns = [
    path("",views.list_food,name='index'),
    path("detael_foot <int:ID>/",views.detail_food,name='detail_lest'),
    path("about/",views.about.as_view(),name='about'),
]

    