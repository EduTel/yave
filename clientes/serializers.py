from .models import Cliente
from rest_framework import routers, serializers, viewsets

class BaseSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, input_formats='%m-%Y', format='%d-%m-%Y %H:%M:%S')
    updated_at = serializers.DateTimeField(read_only=True, input_formats='%m-%Y', format='%d-%m-%Y %H:%M:%S')
    eliminado = serializers.BooleanField(required=True)

class ClienteSerializer(BaseSerializer):

    class Meta:
        """
        """
        model = Cliente
        fields = ["id", "nombre", "apellido_paterno", "apellido_materno", "email", "telefono", "eliminado", "created_at", "updated_at"]

