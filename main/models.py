from django.db import models
import copy

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

    def clone(self, **kwargs):
        obj = self.__class__(**kwargs)
        obj.__dict__.update(self.__dict__)
        obj.pk = None
        return obj
    

class Vacant_report(models.Model):
    Fecha_envio_c = models.DateField(null=True)
    Correo_dest_c = models.EmailField(blank=True)
    Correo_org_c = models.EmailField(blank=True)
    Titula_c = models.CharField(max_length=120)
    telefono_c = models.CharField(max_length=13, default='')
    nom_empresa_c = models.CharField(max_length=60, default='')
    descripcion_c = models.TextField(default='')
    texto_t_c = models.TextField(default='')
    url_vacante_c = models.URLField(max_length=200,  default='')
    url_empresa_c = models.URLField(max_length=200,  default='')
    Report = models.TextField()
    verification = models.BooleanField(default=False)



