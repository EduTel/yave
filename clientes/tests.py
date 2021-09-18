from django.test import TestCase

# Create your tests here.
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from .models import Cliente
from rest_framework.test import APIClient
from pprint import pprint


class TaskApiTests(APITestCase):
    """
        Esta clase es para las pruebas unitarias
    """
    client = APIClient()

    def setUp(self):
        """
            valores de entrada para hacer pruebas unitarias
        """
        Cliente.objects.create(nombre='nombre 1', apellido_paterno="apellido_paterno 1", apellido_materno="apellido_materno 1", telefono="1234567890", email="eduardo_jonathan@outlook.com")
        Cliente.objects.create(nombre='nombre 2', apellido_paterno="apellido_paterno 2", apellido_materno="apellido_materno 2", telefono="234567890", email="eduardo_jonathan2@outlook.com")

    def test_get(self):
        """
            Test sobre el metodo GET
        """
        #url = reverse()
        response = self.client.get('/yave/api/cliente/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        output = {
            "nombre": response.data["nombre"],
            "apellido_paterno": response.data["apellido_paterno"],
            "apellido_materno": response.data["apellido_materno"],
            "telefono": response.data["telefono"],
            "email": response.data["email"],
        }
        self.assertEqual(output, {"nombre": "nombre 1", "apellido_paterno": "apellido_paterno 1", "apellido_materno": "apellido_materno 1", "telefono": "1234567890", "email": "eduardo_jonathan@outlook.com"})

    #def test_update(self):
    #    """
    #        Test sobre el metodo PUT
    #    """
    #    data = {
    #            "descripcion": 'test desc1 :(',
    #            "duracion": 11,
    #            "estatus": 1
    #        }
    #    response = self.client.put('/yave/api/task/1/', data, format='json')
    #    print("response.data",response.data)
    #    output_filter = {
    #        "descripcion": response.data["descripcion"],
    #        "duracion": response.data["duracion"],
    #        "estatus": response.data["estatus"]
    #    }
    #    print("response.status_code", response.status_code)
    #    self.assertEqual(response.status_code, status.HTTP_200_OK)
    #    self.assertEqual(response.data["id"], 1)
    #    self.assertEqual(output_filter, data)

    #def test_delete(self):
    #    """
    #        Test sobre el metodo DELETE primero deberia eliminarse y despues el resultado del metodo GET deberia ser HTTP_404_NOT_FOUND
    #    """
    #    response = self.client.delete('/yave/api/cliente/1/', format='json')
    #    print("response.status_code", response.status_code)
    #    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #    #response = self.client.get('/yave/api/cliente/1/', format='json')
    #    #self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)