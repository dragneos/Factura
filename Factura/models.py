#-*- encoding: utf -*-
import datetime
from django.db import models
from datetime import datetime , timedelta
from django.contrib.auth.models import User
# Create your models here.


class userCedula(models.Model):
    user = models.OneToOneField(User)
    #photo =  models.ImageFIeld(upload_to = url)
    cedula = models.CharField(max_length=11,default="Ingrese la cedula")

class Cliente(models.Model):
    user = models.ForeignKey(User)
    is_cliente = models.IntegerField(max_length=1)

class Categoria(models.Model):
    nombre = models.CharField(max_length=15,default="")
    detalle = models.CharField(max_length=30,default="")
    def is_upperclass(self):
        return self.nombre

class Producto(models.Model):
    Categoria = models.ForeignKey('Categoria')
    descripcion = models.TextField()
    cantidad = models.IntegerField(default=0)
    precio_costo = models.IntegerField(default=0)
    precio_venta = models.IntegerField(default=0)

class Factura(models.Model):
    user = models.ForeignKey(User)
    cliente = models.ForeignKey(Cliente)

class Venta(models.Model):
    user = models.ForeignKey('Factura')
    user = models.ForeignKey('Producto')
    