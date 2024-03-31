from django.db import models

# Create your models here.

class Vacant(models.Model):
    Fecha_envio = models.DateField(null=True)
    Correo_dest = models.EmailField(blank=True)
    Correo_org = models.EmailField(blank=True)
    Titula = models.CharField(max_length=120)
