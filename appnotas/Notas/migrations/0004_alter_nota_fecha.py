# Generated by Django 4.2.7 on 2023-12-01 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notas', '0003_alter_nota_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='Fecha',
            field=models.DateField(),
        ),
    ]
