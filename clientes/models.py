from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class Base(models.Model):
    created_at = models.DateTimeField(verbose_name="Fecha de creacion", auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name="Fecha de actualizacion", auto_now=True, null=True)
    eliminado = models.BooleanField(verbose_name="Eliminado", default=False)

    class Meta:
        abstract = True

# Create your models here.
class Cliente(Base):
    nombre = models.CharField(verbose_name="nombre", max_length=150, null=True, blank=True)
    apellido_paterno = models.CharField(verbose_name="apellido_paterno", max_length=150, null=True, blank=True)
    apellido_materno = models.CharField(verbose_name="apellido_materno", max_length=150, null=True, blank=True)
    telefono = models.CharField(verbose_name="Telefono", max_length=20, null=True, blank=True)
    email = models.CharField(verbose_name="email", max_length=100, null=True, blank=True)
