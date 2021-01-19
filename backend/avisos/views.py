from rest_framework import viewsets

from .models import Area
from .serializers import AreaSerializer


class AreaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Api para acceder a las Áreas,

    Para poder crear y editar registros en el EndPoint
        #class AreaViewSet(viewsets.ModelViewSet):
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer