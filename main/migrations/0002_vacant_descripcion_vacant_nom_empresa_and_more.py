# Generated by Django 4.1.13 on 2024-04-01 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacant',
            name='descripcion',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vacant',
            name='nom_empresa',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='vacant',
            name='telefono',
            field=models.CharField(default='', max_length=13),
        ),
        migrations.AddField(
            model_name='vacant',
            name='texto_t',
            field=models.TextField(default=''),
        ),
    ]
