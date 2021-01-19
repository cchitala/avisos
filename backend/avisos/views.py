from rest_framework import viewsets

from .models import Area, Prioridad, Estado
from .serializers import AreaSerializer, PrioridadSerializer, EstadoSerializer


class AreaViewSet(viewsets.ReadOnlyModelViewSet):
  """
  EndoPoint Areas    
  """
  #class AreaViewSet(viewsets.ModelViewSet):
  queryset = Area.objects.all()
  serializer_class = AreaSerializer

class PrioridadViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Prioridad.objects.all()
  serializer_class = PrioridadSerializer

class EstadoViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Estado.objects.all()
  serializer_class = EstadoSerializer