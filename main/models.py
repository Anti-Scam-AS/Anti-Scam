from django.db import models

# Create your models here.

class Vacant(models.Model):
    Fecha_envio = models.DateField(null=True)
    Correo_dest = models.EmailField(blank=True)
    Correo_org = models.EmailField(blank=True)
    Titula = models.CharField(max_length=120)
    telefono = models.CharField(max_length=13, default='')
    nom_empresa = models.CharField(max_length=60, default='')
    descripcion = models.TextField(default='')
    texto_t = models.TextField(default='')
    url_vacante = models.URLField(max_length=200,  default='')
    url_empresa = models.URLField(max_length=200,  default='')

    def __str__(self):
        return self.Titula
