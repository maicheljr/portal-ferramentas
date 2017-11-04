
from django.contrib.auth import *
from django.conf.urls import url

from . import views

app_name = 'avaliacao'

urlpatterns = [
    #url(r'^$', views.loginUser, name='loginUser'),
    url(r'^listar-ferramenta/$', views.listar_ferramentas, name='listar-ferramenta'),
    #url(r'^listar-ferramenta-js/$', views.listar_ferramentas_js, name='listar-ferramenta-js'),
    url(r'^modal-detalhes-ferramenta/(?P<id_ferramenta>[\w_-]+)?', views.modal_detalhes_ferramenta, name='modal-detalhes-ferramenta'),
    #url(r'^logout/$', views.logoutUser, name='logoutUser'),
    #url(r'^pagamento/$', views.pagamento, name='pagamento'),
    #url(r'^controle-acesso/$', views.controle_acesso, name='controle-acesso'),
    #url(r'^habilitar-usuario/(?P<id_user>[\w_-]+)?', views.habilitar_usuario, name='habilitar-usuario'),
    #url(r'^profile-usuario/(?P<id_user>[\w_-]+)?', views.profile_usuario, name='profile-usuario'),
    #url(r'^recuperar-senha/$', views.lostUser, name='lostUser'),



    #CRUD

    #adicionar
    url(r'^adicionar-categoria/$', views.adicionar_categoria, name='adicionar-categoria'),
    url(r'^adicionar-nivel-dicente/$', views.adicionar_nivel_dicente, name='adicionar-nivel-dicente'),
    url(r'^adicionar-nivel-docente/$', views.adicionar_nivel_docente, name='adicionar-nivel-docente'),
    url(r'^adicionar-ferramenta/$', views.adicionar_ferramenta, name='adicionar-ferramenta'),
    url(r'^adicionar-avaliacao/(?P<id_ferramenta>[\w_-]+)$', views.adicionar_avaliacao, name='adicionar-avaliacao'),
    #url(r'^cadastro-usuario/$', views.registerNewUser, name='cadastrar-usuario-externo'),

    #editar
    url(r'^editar-ferramenta/(?P<id_ferramenta>[\w_-]+)$', views.editar_ferramenta, name='editar-ferramenta'),
    url(r'^editar-categoria/(?P<id_categoria>[\w_-]+)$', views.editar_categoria, name='editar-categoria'),
    url(r'^editar-nivel-dicente/(?P<id_nivel_dicente>[\w_-]+)$', views.editar_nivel_dicente, name='editar-nivel-dicente'),
    url(r'^editar-nivel-docente/(?P<id_nivel_docente>[\w_-]+)$', views.editar_nivel_docente, name='editar-nivel-docente'),

    #listar
    #url(r'^ctrl-usuarios/$', 'ctrl_usuarios', name='ctrl-usuarios'),
    #url(r'^listar-usuario/$', views.listar_usuario, name='listar-usuario'),
    url(r'^detalhes-ferramenta/(?P<id_ferramenta>[\w_-]+)$', views.detalhes_ferramenta, name='detalhes-ferramenta'),
    url(r'^listar-tabela-categoria/$', views.listar_tabela_categoria, name='listar-tabela-categoria'),
    url(r'^listar-tabela-nivel_dicente/$', views.listar_tabela_nivel_dicente, name='listar-tabela-nivel-dicente'),
    url(r'^listar-tabela-nivel_docente/$', views.listar_tabela_nivel_docente, name='listar-tabela-nivel-docente'),
    
    url(r'^listar-tabela-ferramenta/$', views.listar_tabela_ferramentas, name='listar-tabela-ferramenta'),

    ##JS
    #url(r'^listar-ferramenta-filter/$',views.listar_ferramentas_filter, name='listar-ferramenta-'),
    
    #url(r'^listar-ferramenta-default/$',views.listar_ferramentas_default, name='listar-ferramentas-default'),

    ##deletar
    url(r'^excluir-ferramenta/(?P<id_ferramenta>[\w_-]+)$', views.excluir_ferramenta, name='excluir-ferramenta'),
    url(r'^warning-ferramenta/(?P<id_ferramenta>[\w_-]+)$', views.warning_ferramenta, name='warning-ferramenta'),
    
    url(r'^excluir-nivel-dicente/(?P<id_nivel_dicente>[\w_-]+)$', views.excluir_nivel_dicente, name='excluir-nivel-dicente'),
    url(r'^warning-nivel-dicente/(?P<id_nivel_dicente>[\w_-]+)$', views.warning_nivel_dicente, name='warning-nivel-dicente'),

    url(r'^excluir-nivel-docente/(?P<id_nivel_docente>[\w_-]+)$', views.excluir_nivel_docente, name='excluir-nivel-docente'),
    url(r'^warning-nivel-docente/(?P<id_nivel_docente>[\w_-]+)$', views.warning_nivel_docente, name='warning-nivel-docente'),
    
    url(r'^excluir-categoria/(?P<id_categoria>[\w_-]+)$', views.excluir_categoria, name='excluir-categoria'),
    url(r'^warning-categoria/(?P<id_categoria>[\w_-]+)$', views.warning_categoria, name='warning-categoria'),

]