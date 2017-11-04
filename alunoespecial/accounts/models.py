from django.db import models
from django.contrib.auth.models import *
#from vemseragora.planos.models import *
import datetime

class Usuario(User):
    
    objects = UserManager()
    telefone = models.CharField(max_length=16,blank=True)
    cpf = models.CharField(max_length=14, blank=True, null=True, verbose_name='CPF')
    cnpj = models.CharField(max_length=16, blank=True, null=True, verbose_name='CNPJ')    
    endereco = models.CharField(max_length=140, blank=True, null=True, verbose_name=u'Endereço')    
    profissao = models.CharField(max_length=180,blank=True)    
    trocar_senha = models.BooleanField(default=False)
    status = models.BooleanField(default=False, blank=True)
    experiencia = models.TextField(blank=True, null=True,verbose_name='Experiência')

    start_date_acesso = models.DateTimeField(
        'data inicio acesso',default=timezone.now
    )

    final_date_acesso = models.DateTimeField(
        'data final acesso', default=timezone.now
    )

        
    id_rede_social = models.CharField(max_length=32, blank=True)
    
    image = models.ImageField(
        upload_to = 'accounts/img', verbose_name='Imagem',
        null=True,blank=True
    )

    cidade = models.CharField(max_length=50,blank=True)    

    ESTADOS_BRASILEIROS = (
        ('Acre','AC'),	 
		('Alagoas',	'AL'),
		('Amapá','AP'),
		('Amazonas','AM'),
		('Bahia','BA'),
		('Ceará','CE'),
		('Distrito Federal','DF'),
		('Espírito Santo','ES'),
		('Goiás','GO'),
		('Maranhão','MA'),
		('Mato Grosso','MT'),
		('Mato Grosso do Sul','MS'),
		('Minas Gerais','MG'),
		('Pará','PA'),
		('Paraíba','PB'),
		('Paraná','PR'),
		('Pernambuco','PE'),
		('Piauí','PI'),
		('Rio de Janeiro','RJ'),
		('Rio Grande do Norte','RN'),
		('Rio Grande do Sul','RS'),
		('Rondônia','RO'),
		('Roraima','RR'),
		('Santa Catarina','SC'),
		('São Paulo','SP'),
		('Sergipe','SE'),
		('Tocantins','TO'),
		('--- --- ---','---'),

    )
    
    uf = models.CharField(max_length=35, choices=ESTADOS_BRASILEIROS,default='---')

    TIPOS_USUARIOS = (
        ('administrador', 'Administrador'),
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),
        ('usuario', 'usuario'),
    )

    nivel_acesso = models.CharField(max_length=15, choices=TIPOS_USUARIOS,default='professor')
    #categoria = models.ForeignKey(Plano,null=True, blank=True)


    class Meta:
        db_table = "alunoespecial_usuario"
        verbose_name = u"Usuário"
        verbose_name_plural = u"Usuários"
        permissions = (
            ("adicionar_usuario", "Pode adicionar Usuario" ),
            ("editar_usuario", "Pode editar Usuario" ),
            ("visualizar_usuario", "Pode visualizar Usuario" ),
            ("deletar_usuario", "Pode deletar Usuario" ),
        )

    def _str_(self):
        return u"%s" % (self.get_full_name())
        #return u"%s" % dir(self)


