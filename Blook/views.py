from django.shortcuts import render
from Blook.models import Persona ,Experiencia , Educacion,Competencia,Redes_Sociale
from django.http import HttpResponse
# Create your views here.

def principal(request):
    id = 1
    persona = Persona.objects.filter(id=id)
    experiencia = Experiencia.objects.filter(persona_id = id)
    educacion = Educacion.objects.filter(persona_id = id).order_by('ano_egreso')
    competencia1 = Competencia.objects.filter(bloke = 1)
    competencia2 = Competencia.objects.filter(bloke = 2)
    redes_Sociale = Redes_Sociale.objects.filter(persona_id = id)
    
    return render(request,"principal/principal.html",{"personas":persona,"experiencias":experiencia ,"educaciones":educacion ,"compete_one":competencia1 ,"compete_two":competencia2 ,"redes_sociales":redes_Sociale ,"query":id})
