from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('labs', views.mostrar_labs, name='laboratorios'),
    path('add', views.add, name='add'),
    path('edit', views.editar, name='editar_lab'),
]

