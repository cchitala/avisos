from rest_framework import serializers

from .models import Area, Prioridad, Estado

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class PrioridadSerializer(serializers.ModelSerializer):
  class Meta:
      model = Prioridad
      fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Estado,
    fields = '__all__'