from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Plantas(models.Model):  # hereda de moldels.model, en vez del SELF
    especie = models.CharField(max_length=50)
    # elegis CharField o otro desde la lista que te recomienda models, maxLenght es una atributo
    genero = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.especie}, {self.genero}, {self.precio}"

    class Meta:
        verbose_name = "Planta"
        verbose_name_plural = "Plantas"
        ordering = ['-genero']


class Macetas(models.Model):
    nombre = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.material}, {self.precio}"

    class Meta:
        verbose_name = "Maceta"
        verbose_name_plural = "Macetas"


class Jardineria(models.Model):
    # significa que es obligatorio ponerlo
    nombre = models.CharField(max_length=50, blank=False)
    tipo = models.CharField(max_length=50, blank=False)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.tipo}, {self.precio}"

    class Meta:
        verbose_name = "Jardineria"
        verbose_name_plural = "Jardineria"
        ordering = ['-tipo']


class Sustrato(models.Model):
    # significa que es obligatorio ponerlo
    nombre = models.CharField(max_length=50, blank=False)
    tamanio = models.CharField(max_length=50, blank=False)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.tamanio}, {self.precio}"

    class Meta:
        verbose_name = "Sustrato"
        verbose_name_plural = "Sustratos"
        ordering = ['-tamanio']


class Decoracion(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.tipo}, {self.precio}"

    class Meta:
        verbose_name = "Decoracion"
        verbose_name_plural = "Decoracion"
        ordering = ['-tipo']


class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}, {self.email}"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    # on_delete significa que si se elimina el susuario que tambien se elimine su avatar
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
