from django.contrib import admin
from .models import Curso, Aula, Usuario
from django.contrib.auth.admin import UserAdmin

# só existe porque a gente quer que no admin apareça o campo personalizad
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('cursos_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Curso)
admin.site.register(Aula)
admin.site.register(Usuario, UserAdmin)