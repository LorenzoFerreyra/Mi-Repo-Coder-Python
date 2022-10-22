from django.shortcuts import render
from django.http import HttpResponse
from applorenzo.models import Familiar
from applorenzo.forms import Buscar, FamiliarForm
from django.views import View
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

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'applorenzo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})
class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})