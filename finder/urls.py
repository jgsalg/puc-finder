from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='index'),  
    path('add_discipline/', views.add_discipline, name='add_discipline'),
]

