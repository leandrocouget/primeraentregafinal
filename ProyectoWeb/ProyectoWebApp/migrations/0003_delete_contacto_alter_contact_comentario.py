# Generated by Django 4.0.4 on 2022-05-02 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoWebApp', '0002_contacto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contacto',
        ),
        migrations.AlterField(
            model_name='contact',
            name='comentario',
            field=models.TextField(max_length=500),
        ),
    ]