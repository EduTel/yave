# Generated by Django 3.2.7 on 2021-09-18 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualizacion')),
                ('eliminado', models.BooleanField(default=False, verbose_name='Eliminado')),
                ('nombre', models.CharField(blank=True, max_length=150, null=True, verbose_name='nombre')),
                ('apellido_paterno', models.CharField(blank=True, max_length=150, null=True, verbose_name='apellido_paterno')),
                ('apellido_materno', models.CharField(blank=True, max_length=150, null=True, verbose_name='apellido_materno')),
                ('telefono', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
