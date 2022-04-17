from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Usuario(AbstractUser):
    nombres =  models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=30
    )
    apellidos = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=30
    )
    cedula = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=10
    )
    domicilio = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=30
    )
    telefono = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=10
    )
    fecha_nacimiento = models.DateField(default=timezone.now())

class Dependencia(models.Model):
    descripcion =  models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45
    )
    estado = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=1
    )

class Jornada(models.Model):
    observacion = models.CharField(
        unique=False, 
        null=False,
        blank=True,
        max_length=45
    )
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    dia_semana = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=10
    )
    estado = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=1
    )

class Horario(models.Model):
    observacion = models.CharField(
        unique=False, 
        null=False,
        blank=True,
        max_length=45)
    estado = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=1
    )
    idJornadas = models.ForeignKey(Jornada, on_delete=models.CASCADE, related_name="fk_jornada_Horario")

class Cargo(models.Model):
    nombre_cargo = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=35
    )
    descripcion = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45
    )
    estado = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=1
    )
    idDependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE, related_name="fk_Dependencia_Cargo")
    idHorario =  models.ForeignKey(Horario, on_delete=models.CASCADE, related_name="fk_Horario_Cargo")

class EmpleadoConCargo(models.Model):
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="fk_Cargo_EmpleadoConCargo")
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="fk_Usuario_EmpleadoConCargo")

class PermisosEmpleado(models.Model):
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    motivo = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45
    )
    idEmpleado = models.ForeignKey(EmpleadoConCargo, on_delete=models.CASCADE, related_name="fk_Empleado_PermisosEmpleado")
    estado = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=1
    )

class VacacionesEmpleado(models.Model):
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    idEmpleado = models.ForeignKey(EmpleadoConCargo, on_delete=models.CASCADE, related_name="fk_Empleado_VacacionesEmpleado")
    estado =  models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=1
    )

class Docente(models.Model):
    idEmpleado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="fk_Empleado_Docente")
    estado =  models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=1
    )

class Materia(models.Model):
    nombre_materia =  models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=30
    )
    estado =  models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=1
    )

class Curso(models.Model):
    semestre = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=6
    )
    hora_inicio =  models.TimeField()
    hora_final = models.TimeField()
    dia_semana = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=10)
    salon = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=4
        )
    sede = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=10
        )
    cupos = models.IntegerField()
    creditos = models.IntegerField()
    idDocente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name="fk_Docente_Curso")
    idMateria = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="fk_Materia_Curso")

class PermisosDocente(models.Model):
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    motivo = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45
    )
    idDocente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name="fk_Docente_PermisosDocente")
    estado =  models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=1
    )

class VacacionesDocente(models.Model):
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    idDocente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name="fk_Docente_VacacionesDocente")
    estado =  models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=1
    )

class AsistenciaDocente(models.Model):
    asistencia = models.BooleanField()
    idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="fk_Curso_AsistenciaDocente")
    tema = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=20
    )
    dificultades = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45
    )

class AsitenciaEmpleado(models.Model):
    asistencia = models.BooleanField()
    idEmpleado = models.ForeignKey(EmpleadoConCargo, on_delete=models.CASCADE, related_name="fk_Empleado_AsistenciaEmpleado")
    observacion = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45
    )