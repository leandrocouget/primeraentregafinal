# Generated by Django 4.0.4 on 2022-05-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoWebApp', '0003_delete_contacto_alter_contact_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='comentario',
            field=models.CharField(max_length=500),
        ),
    ]
