from django.shortcuts import render
from django.http import HttpResponse
from applorenzo.models import Familiar
# Create your views here.
def saludo(request):
    return HttpResponse("Hola, esta es mi primer app")

def saludo_dos(request):
    return HttpResponse("Esta es mi segunda función")
def saludar_a(request, name):
    return HttpResponse(f"Hola, ¿cómo estás, {name}")
def mostrar_mi_template(request):
    return render(request, 'applorenzo/index.html')
def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "applorenzo/familiares.html", {"lista_familiares": lista_familiares})