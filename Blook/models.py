from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.

class Persona(models.Model):
    rut = models.CharField(max_length=18)
    primer_nombre = models.CharField(max_length=55)
    segundo_nombre = models.CharField(max_length=55)
    primer_apellido = models.CharField(max_length=55)
    segundo_apellido = models.CharField(max_length=55)
    biografia = models.TextField()
    fecha_Nacimiento = models.DateField()
    bio_Laboral = models.TextField(null= True)
    bio_Educacion = models.TextField(null=True)
    bio_Habilidades  = models.TextField(null=True)

class Experiencia(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=55)
    cargo = models.CharField(max_length=55)
    periodo_inicio = models.DateField()
    periodo_fin  = models.DateField()
    descripcion = models.TextField()
    web = models.TextField(max_length=100,null=True)

class Educacion(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nombre_institucion = models.CharField(max_length=55)
    carrera = models.CharField(max_length=55)
    ano_ingreso = models.IntegerField()
    ano_egreso = models.IntegerField()
    ruta_logo = models.IntegerField(null=True)

class Competencia(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nombre_tecnologia = models.CharField(max_length=55)
    porcentaje_conocimiento = models.IntegerField()
    anos_experiencia = models.IntegerField()
    bloke = models.IntegerField(null=True)
    

class Redes_Sociale(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=55)
    referencia = models.CharField(max_length=55)