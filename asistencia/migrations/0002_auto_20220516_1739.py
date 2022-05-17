# Generated by Django 3.2.12 on 2022-05-16 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta_usuario',
            name='cedula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_cedula', to='asistencia.empleado'),
        ),
        migrations.AlterField(
            model_name='cuenta_usuario',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]