# Generated by Django 3.2.7 on 2021-09-18 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='clientes',
            new_name='cliente',
        ),
    ]