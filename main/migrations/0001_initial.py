# Generated by Django 4.1.13 on 2024-03-31 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_envio', models.DateField(null=True)),
                ('Correo_dest', models.EmailField(blank=True, max_length=254)),
                ('Correo_org', models.EmailField(blank=True, max_length=254)),
                ('Titula', models.CharField(max_length=120)),
            ],
        ),
    ]
