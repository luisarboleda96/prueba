from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from .pqrsf import PQRSF_CHOICES
# Create your models here.

class Contact(models.Model):
    email = models.EmailField(max_length = 50, verbose_name = "correo electronico")
    tipom = models.CharField(max_length = 50, choices = PQRSF_CHOICES,default="peticion",verbose_name="categorias")
    nombre = models.CharField(max_length = 250, verbose_name = "Nombre")
    msj = RichTextField(default="Quisiera",verbose_name = "Mensaje")

    class Meta:
        verbose_name = "Mensajes PQRSF"
        verbose_name_plural = "Mensajes PQRSF"

class Etnia(models.Model):
    NombEtni = models.CharField(max_length = 50)

def __str__(self):
    return self.nombre