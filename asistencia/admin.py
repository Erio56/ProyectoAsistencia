from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Usuario)
admin.site.register(models.Dependencia)
admin.site.register(models.Cargo)
admin.site.register(models.Curso)
admin.site.register(models.Horario)
admin.site.register(models.Jornada)
admin.site.register(models.EmpleadoConCargo)
admin.site.register(models.VacacionesDocente)
admin.site.register(models.VacacionesEmpleado)
admin.site.register(models.PermisosDocente)
admin.site.register(models.PermisosEmpleado)
admin.site.register(models.Docente)
admin.site.register(models.Materia)
admin.site.register(models.AsistenciaDocente)
admin.site.register(models.AsitenciaEmpleado)