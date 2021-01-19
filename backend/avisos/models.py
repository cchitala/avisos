from django.db import models

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