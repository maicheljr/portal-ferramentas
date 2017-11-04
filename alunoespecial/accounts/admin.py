from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario','uf','email', 'status','nivel_acesso']


admin.site.register(Usuario, UsuarioAdmin)
