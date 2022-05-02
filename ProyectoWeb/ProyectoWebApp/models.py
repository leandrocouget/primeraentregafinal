from django.db import models

# Create your models here.
class register(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    email = models.EmailField(null=False,blank=False)
    

    def __str__(self):
        return self.nombre + "-" + self.apellido

class articles(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)
    cantidad = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre + "-" + self.precio + "-" + self.cantidad

class contact(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    email = models.EmailField(null=False,blank=False)
    comentario = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre + "-" + self.email
        
    
