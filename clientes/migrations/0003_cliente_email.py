# Generated by Django 3.2.7 on 2021-09-18 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_rename_clientes_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='email'),
        ),
    ]
