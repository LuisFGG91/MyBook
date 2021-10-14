from django.shortcuts import render
#from model.models import Persona
from django.http import HttpResponse
# Create your views here.

def inicioSesion(request):
    id = 1
 #   persona = Persona.objects.filter(id=id)
    
    return render(request,"inicioSesion/inicioSesion.html",{"query":id})


def principal(request):
    id = 1
  #  persona = Persona.objects.filter(id=id)
    
    return render(request,"principal/principal.html",{"query":id})
