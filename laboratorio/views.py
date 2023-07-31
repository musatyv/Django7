from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse  # noqa: F401, F401

from laboratorio.models import Laboratorio, DirectorGeneral, Producto
# Create your views here.

def index(request):
    context = {"title": "Inicio"}
    return render(request,'lab/index.html',context)

def add(request):
    return render(request, 'lab/add_lab.html')

def editar(request):
    return render(request, 'lab/editar_lab.html')


def mostrar_labs(request):
    context = {"title": "Laboratorios"}
    return render(request, 'lab/laboratorios.html', context)


def obtener_labs(): 
    laboratorios = Laboratorio.objects.all()
    labs_ordenados = laboratorios.order_by('nombre')
    ...
    
def eliminar_lab(lab: Laboratorio):
    try:
        lab.delete()
        HttpResponseRedirect("labs/")
    except AssertionError:
        ...
    ...
    