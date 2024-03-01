from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hardware(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    precio =models.FloatField()
    def __str__(self):
        return f"Producto : {self.nombre}, {self.tipo}"

class Serviciotecnico(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    precio =models.FloatField()
    estado=models.CharField(max_length=50)
    def __str__(self):
        return f"Servicio : {self.nombre}, Estado Actual: {self.estado} ,Descripcion : {self.descripcion} "

class Proyectos(models.Model):
    nombre = models.CharField(max_length=50)
    lenguaje = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    horas= models.FloatField()
    estado=models.CharField(max_length=50)
    def __str__(self):
     return f"Proyecto : {self.nombre}, Lenguaje: {self.lenguaje},  Estado Actual: {self.estado} ,Descripcion : {self.descripcion} "
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"   



