# Generated by Django 4.2.5 on 2023-09-22 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, unique=True, verbose_name='Nombre Departamento')),
                ('area', models.CharField(blank=True, max_length=30, null=True, verbose_name='Area')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
        ),
    ]