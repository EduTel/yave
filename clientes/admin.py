from django.contrib import admin

from .models import Cliente
# Register your models here.

class admin_cliente(admin.ModelAdmin):
    list_display = [field.name for field in Cliente._meta.fields]

admin.site.register(Cliente, admin_cliente)
