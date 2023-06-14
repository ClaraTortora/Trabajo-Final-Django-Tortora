# Generated by Django 4.2.2 on 2023-06-14 13:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_alter_producto_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='fecha_actualizacion',
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha_de_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Fecha de publicación'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen_producto',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='productocategoria',
            name='fecha_de_actualizacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Fecha de actualización'),
        ),
    ]
