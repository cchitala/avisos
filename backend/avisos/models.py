from django.db import models
from django.contrib.auth.models import User

class Area(models.Model):
  area = models.CharField(max_length=255)
  descripcion = models.TextField()
  estatus = models.SmallIntegerField(default=1)

  def __str__(self):
    return self.area

  
class Prioridad(models.Model):
  prioridad = models.CharField(max_length=50)
  orden = models.SmallIntegerField(default=0)

  def __str__(self):
    return self.prioridad

  class Meta:
      verbose_name_plural = "Prioridades"

class Estado(models.Model):
  estado = models.CharField(max_length=100)
  descripcion = models.CharField(max_length=100)
  status = models.SmallIntegerField(default=1) 

  def __str__(self):
    return self.estado

class Aviso(models.Model):
  creador = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
  aviso = models.CharField(max_length=255)
  descripcion = models.TextField()
  estado = models.ForeignKey(Estado, blank=True, null=True, on_delete=models.SET_NULL)
  areas = models.ManyToManyField(Area)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.aviso

class Nota(models.Model):
  aviso = models.ManyToManyField(Aviso)
  nota = models.TextField()
  creador = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

  def __str__(self):
    return self.aviso
  