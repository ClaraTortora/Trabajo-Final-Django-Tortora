# Generated by Django 4.2.2 on 2023-06-14 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0008_alter_producto_modelo_ofertas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ofertas',
            name='imagen_oferta',
            field=models.ImageField(blank=True, null=True, upload_to='celulares'),
        ),
    ]
