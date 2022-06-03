# Generated by Django 4.0.5 on 2022-06-03 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacion', models.CharField(max_length=60)),
                ('libro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='libros.libro')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellidos', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Prestar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDev', models.DateField()),
                ('fechaPres', models.DateField()),
                ('ejemplar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prestar.ejemplar')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prestar.usuario')),
            ],
        ),
    ]
