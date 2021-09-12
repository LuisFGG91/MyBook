from django.contrib import admin

# Register your models here.

from Blook.models import Persona,Experiencia,Educacion,Competencia,Redes_Sociale

admin.site.register(Persona)
admin.site.register(Educacion)
admin.site.register(Competencia)
admin.site.register(Experiencia)
admin.site.register(Redes_Sociale)