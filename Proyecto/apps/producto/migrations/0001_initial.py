# Generated by Django 4.2.2 on 2023-06-08 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=50, unique=True)),
                ('descripcion_producto', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
