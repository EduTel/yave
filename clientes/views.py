from django.shortcuts import render
from .models import Cliente
from rest_framework.response import Response
from .serializers import ClienteSerializer
from rest_framework import exceptions, status, views
from rest_framework.authentication import TokenAuthentication
from rest_framework import routers, serializers, viewsets

from rest_framework import permissions

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    """
        aqui se establecen todos los campos a ser mostrados en la api con Django Rest Framework
    """

    #authentication_classes = [TokenAuthentication, ]
    #permission_classes = [permissions.DjangoModelPermissions, ]

    def get_serializer_class(self):
        return ClienteSerializer

    def get_queryset(self):
        #print("========================================ClienteViewSet list")
        return Cliente.objects.filter()

    def destroy(self, request, pk=None):
        print("========================================ClienteViewSet destroy")
        f_cliente = Cliente.objects.filter(pk=pk, eliminado=False)
        if f_cliente.exists():
            f_cliente.update(eliminado=True)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        #print("========================================ClienteViewSet list")
        #print(request.query_params)
        id = request.query_params.get('id')
        eliminado = request.query_params.get('eliminado')
        if id:
            queryset = Cliente.objects.filter(pk=id)
        elif eliminado:
            queryset = Cliente.objects.filter(eliminado=eliminado)
        else:
            queryset = Cliente.objects.filter(eliminado=False)
        serializer = ClienteSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def get_permissions(self):
        #print("========================================ClienteViewSet get_permissions")
        """
            Instantiates and returns the list of permissions that this view requires.
        """
        print(self.action)
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]