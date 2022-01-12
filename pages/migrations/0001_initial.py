# Generated by Django 3.2.4 on 2021-06-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('idPag', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id de Pagina')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo de pagina')),
                ('descripcion', models.TextField(verbose_name='Descripcion del Pagina')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='URL AMIGABLE')),
                ('estado', models.BooleanField(verbose_name='Estado de la pagina')),
            ],
        ),
    ]