from turtle import mode
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager,)
from django.utils import timezone
from django.conf import settings

# Create your models here.
class empleado(models.Model):
    cedula = models.CharField(
        primary_key=True,
        unique=True, 
        null=False,
        blank=False,
        max_length=15
    )
    nombres =  models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45
    )
    apellidos = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45
    )
    direccion = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45
    )
    telefono = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45
    )
    fecha_nacimiento = models.DateField()
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1
        )
    email =  models.EmailField()
    def __str__(self):
        # String to give nick attr to admin site
        return self.nombres
    
class CustomAccountManager(BaseUserManager):
    def create_user(self, nombre_usuario,cedula, password, **other_fields):
        usuario = self.model(nombre_usuario=nombre_usuario,cedula=cedula, **other_fields)
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self, nombre_usuario,cedula, password, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        return self.create_user(nombre_usuario,empleado.objects.get(cedula=cedula),password, **other_fields)
class cuenta_usuario(AbstractBaseUser,PermissionsMixin):
    nombre_usuario = models.CharField(
        unique=True, 
        null=False,
        blank=False,
        
        max_length=45
    )
    cedula = models.ForeignKey(empleado, on_delete=models.CASCADE, related_name='fk_cedula')
    password = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=255
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = CustomAccountManager()

    USERNAME_FIELD='nombre_usuario'
    REQUIRED_FIELDS=['cedula']
    def __str__(self):
    # String to give nick attr to admin site
        return self.nombre_usuario
    
class Dependencia(models.Model):
    nombre_dependencia = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45)
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1
        )

class Cargo(models.Model):
    nombre_cargo = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45)
    dependencia =  models.ForeignKey(Dependencia, on_delete=models.CASCADE, related_name='fk_dependencia')
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1
        )
    
class Materia(models.Model):
    codigo_materia = models.CharField(
        primary_key=True,   
        unique=False, 
        null=False,
        blank=False,
        max_length=45)
    nombre_materia = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45)
    estado = models.CharField(        
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
        max_length=10)
    sede = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=10)
    codigo_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='fk_materia')
    cedula_docente = models.ForeignKey(empleado, on_delete=models.CASCADE, related_name='fk_docente')
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    salon = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=10)
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1
        )
    
class Horario(models.Model):
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    fecha = models.DateField()
    observacion = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45)
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1
        )

class Detalle_Cargo_Empleado(models.Model):
    cedula_empleado = models.ForeignKey(empleado, on_delete=models.CASCADE, related_name="fk_detalle_empleado_cargo")
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="fk_detalle_cargo")
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1
        )
    
class Detalle_Horario_Empleado(models.Model):
    cedula_empleado = models.ForeignKey(empleado, on_delete=models.CASCADE, related_name="fk_horario_empleado_cedula")
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, related_name="fk_horario_empleado")
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1
        )
class Asistencia_Empleado(models.Model):
    cedula = models.ForeignKey(empleado, on_delete=models.CASCADE, related_name="fk_asistencia_cedula")
    fecha_hora_asitencia = models.DateTimeField()
    observacion = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45)
class Asistencia_Docente(models.Model):
    cedula = models.ForeignKey(empleado, on_delete=models.CASCADE, related_name="fk_asistencia_cedula_docente")
    fecha_hora_asitencia = models.DateTimeField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="fk_asistencia_docente_curso")
    observacion = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45)
    
class PermisoEmpleado(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    cedula = models.ForeignKey(empleado, on_delete=models.CASCADE, related_name="fk_permiso_empleado")
    descripcion = models.TextField(blank=False, max_length=300)
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1
        )
    
class VacacionesEmpleado(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    cedula = models.ForeignKey(empleado, on_delete=models.CASCADE, related_name="fk_vacacion_empleado")
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1
        )
    