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
    state = models.BooleanField(default=False)

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
    state_c = models.BooleanField(default=False)
    Report = models.TextField()
    verification = models.BooleanField(default=False)

    def __str__(self):
        return self.Titula_c

class update_vacante_command:
    def __init__(self, Vacant_report, Report, verification):
        self.Vacant_report = Vacant_report
        self.Vacant_report.Report = Report
        self.Vacant_report.verification = verification

    def execute(self):
        self.Vacant_report.save()


class delete_vacante_command:
    def __init__(self, Vacant_report):
        self.Vacant_report = Vacant_report

    def execute(self):
        self.Vacant_report.delete()
        

class Admin(models.Model):
    email = models.EmailField(unique=True)
    vacants_wait = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.email
    
    def update_sub(self, vacants_wait):
        if self.vacants_wait:
            vacants_list = self.vacants_wait.split(',')
            if vacants_wait not in vacants_list:
                vacants_list.append(vacants_wait)
        else:
            vacants_list = [vacants_wait]

        self.vacants_wait = ','.join(vacants_list)
        self.save()

    def delete_sub(self, vacants_wait):
        if self.vacants_wait:
            vacants_list = self.vacants_wait.split(',')
            if vacants_wait in vacants_list:
                vacants_list.remove(vacants_wait)

            self.vacants_wait = ','.join(vacants_list)
            self.save()
