from django.contrib import admin
from alunoespecial.avaliacao.models import *


from .models import *

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['ferramenta','avaliacao_pro','avaliacao_contra','recomendacoes','upload_at','created_at']
    search_fields = ['ferramenta']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome','descricao']
    search_fields = ['nome','descricao']

class NivelDocenteAdmin(admin.ModelAdmin):
    list_display = ['nome','descricao']
    search_fields = ['nome','descricao']

class NivelDicenteAdmin(admin.ModelAdmin):
    list_display = ['nome','descricao']
    search_fields = ['nome','descricao']

class FerramentaAdmin(admin.ModelAdmin):
    list_display = ['nome','descricao','link_download','categoria','nivel_professor','nivel_aluno','requisitos_sistema','indicacao_pedagogica']
    #list_display = ['nome','descricao','link_download','categoria','requisitos_sistema','indicacao_pedagogica']
    search_fields = ['nome','descricao']


admin.site.register(Avaliacao,AvaliacaoAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(NivelDicente,NivelDicenteAdmin)
admin.site.register(NivelDocente, NivelDocenteAdmin)
admin.site.register(Ferramenta,FerramentaAdmin)
