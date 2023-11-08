# Generated by Django 4.2.5 on 2023-10-04 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('controlDepartamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, unique=True, verbose_name='Nombre Empleado')),
                ('tipo', models.CharField(choices=[('2', 'Tiempo Completo'), ('3', 'Otro'), ('1', 'Medio Tiempo')], max_length=1, verbose_name='Tipo de Contrato')),
                ('dato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlDepartamento.departamento')),
            ],
        ),
    ]