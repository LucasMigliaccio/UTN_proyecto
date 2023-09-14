from django.db import models

# Create your models here.

class Saludos(models.Model):
    tipo = models.CharField(max_length=40)
    img= models.ImageField(upload_to="tienda/images/", max_length=255)

class CategoriaBebidas(models.Model):
    tipo= models.CharField(max_length=20)

    def __str__(self):
        return self.tipo

class Producto(models.Model):
    nombre= models.CharField(max_length=20)
    img= models.ImageField(upload_to="tienda/images/", max_length=255)
    categoria= models.ForeignKey(CategoriaBebidas, on_delete=models.CASCADE)
    saludable= models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
