# Generated by Django 4.2.5 on 2023-10-04 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controlDepartamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['nom'], 'verbose_name': 'Departamentos', 'verbose_name_plural': 'Departamentos Empresas'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('nom', 'area')},
        ),
    ]