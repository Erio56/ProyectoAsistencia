from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(empleado)
admin.site.register(cuenta_usuario)
admin.site.register(Dependencia)
admin.site.register(Cargo)
admin.site.register(Materia)
admin.site.register(Curso)
admin.site.register(Horario)
admin.site.register(Detalle_Cargo_Empleado)
admin.site.register(Detalle_Horario_Empleado)
admin.site.register(Asistencia_Empleado)
admin.site.register(Asistencia_Docente)
admin.site.register(PermisoEmpleado)
admin.site.register(VacacionesEmpleado)

