# Generated by Django 3.2 on 2021-04-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.CharField(max_length=12, verbose_name='Latitud')),
                ('longitud', models.CharField(max_length=12, verbose_name='Longitud')),
            ],
            options={
                'verbose_name': 'Ubicación',
                'verbose_name_plural': 'Datos de la ubicación',
            },
        ),
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacidad', models.TextField(max_length=5000, verbose_name='Política de privacidad')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la aplicación')),
                ('nombreContro', models.CharField(max_length=20, verbose_name='Nombre corto')),
                ('telefono', models.CharField(max_length=100, verbose_name='Contacto')),
            ],
            options={
                'verbose_name': 'Información',
                'verbose_name_plural': 'Datos de la aplicación',
            },
        ),
        migrations.CreateModel(
            name='Temperatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperaturaMinima', models.DecimalField(decimal_places=2, default=0.0, max_digits=2, verbose_name='Temperatura mínima')),
                ('temperaturaMaxima', models.DecimalField(decimal_places=2, default=0.0, max_digits=2, verbose_name='Temperatura máxima')),
                ('temperaturaLeida', models.DecimalField(decimal_places=2, default=0.0, max_digits=2, verbose_name='Temperatura leída')),
            ],
            options={
                'verbose_name': 'Temperatuta',
                'verbose_name_plural': 'Temperaturas',
            },
        ),
    ]