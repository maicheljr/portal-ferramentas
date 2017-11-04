
from django.contrib.auth import *
from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    #url(r'^$', views.loginUser, name='loginUser'),
    url(r'^login/$', views.loginUser, name='loginUser'),
    url(r'^$', views.loginUser, name='loginUser'),
    url(r'^adicionar-usuario/$', views.adicionar_usuario, name='adicionar-usuario'),
    url(r'^adicionar-usuario-interno/$', views.adicionar_usuario_interno, name='adicionar-usuario-interno'),
    url(r'^logout/$', views.logoutUser, name='logoutUser'),
    #url(r'^pagamento/$', views.pagamento, name='pagamento'),
    #url(r'^controle-acesso/$', views.controle_acesso, name='controle-acesso'),
    #url(r'^habilitar-usuario/(?P<id_user>[\w_-]+)?', views.habilitar_usuario, name='habilitar-usuario'),
    url(r'^profile/(?P<id_usuario>[\w_-]+)?', views.profile, name='profile'),
    #url(r'^recuperar-senha/$', views.lostUser, name='lostUser'),
    #url(r'^profile/$', views.profile, name='profile'),

    #CRUD

    #adicionar
    #url(r'^adicionar-usuario/$', views.registerUser, name='adicionar-usuario'),
    #url(r'^cadastro-usuario/$', views.registerNewUser, name='cadastrar-usuario-externo'),

    #editar
    url(r'^editar-usuario/(?P<id_usuario>[\w_-]+)$', views.editar_usuario_interno, name='editar-usuario'),

    #listar
    #url(r'^ctrl-usuarios/$', 'ctrl_usuarios', name='ctrl-usuarios'),
    url(r'^listar-usuarios/$', views.listar_usuarios, name='listar-usuarios'),
    url(r'^warning/(?P<id_usuario>[\w_-]+)$', views.warning, name='warning'),
    #url(r'^ctrl-usuario/$', views.ctrl_usuario, name='ctrl-usuario'),

    ##deletar
    url(r'^excluir-usuario/(?P<id_usuario>[\w_-]+)$', views.excluir_usuario, name='excluir-usuario'),

]