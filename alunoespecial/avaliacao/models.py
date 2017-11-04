from django.db import models
from alunoespecial.accounts.models import *
from django.conf import settings



class AvaliacaoManager(models.Manager):  

    def search(self, query):
        return  self.get_queryset().filter(
            models.Q(ferramenta__icontains=query) 
            
        )

class Categoria(models.Model):    
    
    nome = models.CharField('nome', max_length=100,blank=True)          
    descricao = models.TextField(blank=True, null=True)

        
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    upload_at = models.DateTimeField(
        'Atualizado em', auto_now = True
    )

    

    def __str__(self):
        return self.nome.upper()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']



class NivelDicente(models.Model):    
    
    nome = models.CharField('nome', max_length=100,blank=True)          
    descricao = models.TextField(blank=True, null=True)

        
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    upload_at = models.DateTimeField(
        'Atualizado em', auto_now = True
    )

    

    def __str__(self):
        return self.nome.upper()

    class Meta:
        verbose_name = 'Nível Dicente'
        verbose_name_plural = 'Níveis Dicente'
        ordering = ['nome']


class NivelDocente(models.Model):    
    
    nome = models.CharField('nome', max_length=100,blank=True)          
    descricao = models.TextField(blank=True, null=True)

        
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    upload_at = models.DateTimeField(
        'Atualizado em', auto_now = True
    )

    

    def __str__(self):
        return self.nome.upper()

    class Meta:
        verbose_name = 'Nível Docente'
        verbose_name_plural = 'Níveis Docente'
        ordering = ['nome']


class Ferramenta(models.Model):
    
    nome = models.CharField('nome', max_length=100,blank=True)          
    descricao = models.TextField('descrição',blank=True, null=True)
    link_download = models.CharField('link_download', max_length=100,blank=True)          
    categoria = models.ForeignKey(Categoria,blank=True)    
    imagem = models.ImageField(upload_to='avaliacao/imagens',
                             blank=True,
                             null=True,
                             verbose_name=u'Adicionar imagem')


    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    upload_at = models.DateTimeField(
        'atualizado em', auto_now = True
    )

    #NIVEL_PROFESSOR = (
    #    ('iniciante', 'Iniciante'),
    #    ('intermediário', 'Intermediário'),        
    #    ('profissional', 'Profissional'),
    #)

    nivel_professor = models.ForeignKey(NivelDocente,blank=True, null=True)
    #categoria = models.ForeignKey(Categoria,blank=True)    

    #NIVEL_ALUNO = (
    #    ('iniciante', 'Iniciante'),
    #    ('intermediário', 'Intermediário'),        
    #    ('profissional', 'Profissional'),
    #)
    nivel_aluno = models.ForeignKey(NivelDicente,blank=True, null=True)
    

    requisitos_sistema = models.TextField('requisitos do sistema',blank=True, null=True)
    indicacao_pedagogica = models.TextField('Indicação de Ensino Pedagógico', max_length=100,blank=True)          



    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Ferramenta'
        verbose_name_plural = 'Ferramentas'
        ordering = ['nome'] 
        

class Avaliacao(models.Model):    
    
    usuario = models.ForeignKey(Usuario, null=True, blank=True)
    ferramenta = models.ForeignKey(Ferramenta,blank=False)    
    avaliacao_pro = models.TextField(blank=True, null=True)
    avaliacao_contra = models.TextField(blank=True, null=True)
    recomendacoes = models.TextField(blank=True, null=True)

    last_update = models.DateTimeField(
        'Ultima atualização', auto_now = True
    )
    
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    upload_at = models.DateTimeField(
        'Atualizado em', auto_now = True
    )

    objects = AvaliacaoManager()

    def __str__(self):
        return self.avaliacao_pro

    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliações'
        ordering = ['ferramenta']







