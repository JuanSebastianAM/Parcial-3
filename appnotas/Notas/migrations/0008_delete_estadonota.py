# Generated by Django 4.2.7 on 2023-12-01 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notas', '0007_remove_nota_fecha'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EstadoNota',
        ),
    ]