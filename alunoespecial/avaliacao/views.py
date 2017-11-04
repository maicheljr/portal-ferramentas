from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import *
from django.shortcuts import render, redirect
from alunoespecial.avaliacao.models import *

from decimal import *
from .forms import *
from alunoespecial.avaliacao.forms import *

import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import  HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext



def listar_ferramentas (request):


    if request.POST:
        
       
        ferramenta = Ferramenta.objects.all()

        if request.POST['categoria']:
            ferramenta = ferramenta.filter(categoria__nome=request.POST['categoria'])

        if request.POST['nivel_docente']:
            ferramenta = ferramenta.filter(nivel_professor__nome=request.POST['nivel_docente'])

        if request.POST['nivel_dicente']:
            ferramenta = ferramenta.filter(nivel_aluno__nome=request.POST['nivel_dicente'])
        
        if request.POST['palavra']:
            ferramenta = ferramenta.filter(nome__icontains=request.POST['palavra'])



    else:
        ferramenta = Ferramenta.objects.all()

   
    context = {

        'categoria': Categoria.objects.all(),
        'nivel_docente': NivelDocente.objects.all(),
        'nivel_dicente': NivelDicente.objects.all(),
        'ferramenta':ferramenta,
        
    }

    template_name = 'listar-ferramentas.html'

    return render(request, template_name,context)






def listar_tabela_ferramentas (request):


   
    context = {

        #'categoria': Categoria.objects.all(),
        'ferramentas':Ferramenta.objects.all(),
        
    }

    template_name = 'listar-tabela-ferramentas.html'

    return render(request, template_name,context)


def listar_tabela_categoria (request):


   
    context = {

        'categoria': Categoria.objects.all(),
        #'ferramentas':Ferramenta.objects.all(),
        
    }

    template_name = 'listar-tabela-categoria.html'

    return render(request, template_name,context)



def detalhes_ferramenta (request,id_ferramenta):

    template_name = 'detalhes-ferramenta.html'

    try:

        ferramenta = Ferramenta.objects.get(id=id_ferramenta)
        avaliacao = Avaliacao.objects.filter(ferramenta__id=id_ferramenta)

        pro = 0
        contra = 0

        for a in avaliacao:
            if a.avaliacao_pro :
                pro = pro + 1        
            if a.avaliacao_contra :
                contra = contra +1

        context = {
        
        'f':ferramenta,
        'avaliacao': avaliacao,
        'pro': pro,
        'contra': contra,
        }


        return render(request, template_name,context)

        
        
    except:
        raise 
        messages.error(request, u" Impossível fazer a busca, contate o administrador do sistema")
        return redirect('avaliacao:listar-ferramenta')
   
    



@login_required(login_url ='/conta/login/')
def adicionar_categoria (request):    

    form = AdicionarCategoriaForm()

    if request.method == 'POST':
        form = AdicionarCategoriaForm(data = request.POST)
        if form.is_valid():
            form.save()
                    
            form = AdicionarCategoriaForm()
            messages.success(request,' Dados inseridos com sucesso!!!')
            return redirect('avaliacao:listar-tabela-categoria')
        else:
            messages.error(request, 'Erro ao cadastrar !!!')

    template_name = 'adicionar-categoria.html'
    context = {

        #'propriedade': Propriedade.objects.filter(usuario=request.user),
        'form': form,

    }
    return render(request, template_name, context)

@login_required(login_url ='/conta/login/')
def adicionar_nivel_dicente (request):    

    form = AdicionarNivelDicenteForm()

    if request.method == 'POST':
        form = AdicionarNivelDicenteForm(data = request.POST)
        if form.is_valid():
            form.save()
                    
            form = AdicionarNivelDicenteForm()
            messages.success(request,' Dados inseridos com sucesso!!!')
            return redirect('avaliacao:listar-tabela-nivel-dicente')
        else:
            messages.error(request, 'Erro ao cadastrar !!!')

    template_name = 'adicionar-nivel-dicente.html'
    context = {

        #'propriedade': Propriedade.objects.filter(usuario=request.user),
        'form': form,

    }
    return render(request, template_name, context)

@login_required(login_url ='/conta/login/')
def adicionar_nivel_docente (request):    

    form = AdicionarNivelDocenteForm()

    if request.method == 'POST':
        form = AdicionarNivelDocenteForm(data = request.POST)
        if form.is_valid():
            form.save()
                    
            form = AdicionarNivelDocenteForm()
            messages.success(request,' Dados inseridos com sucesso!!!')
            return redirect('avaliacao:listar-tabela-nivel-docente')
        else:
            messages.error(request, 'Erro ao cadastrar !!!')

    template_name = 'adicionar-nivel-docente.html'
    context = {

        #'propriedade': Propriedade.objects.filter(usuario=request.user),
        'form': form,

    }
    return render(request, template_name, context)


def adicionar_avaliacao (request,id_ferramenta):    

    form = AdicionarAvaliacaoForm()


    ferramenta = Ferramenta.objects.get(id=id_ferramenta)


    if request.method == 'POST':
        form = AdicionarAvaliacaoForm(data = request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.ferramenta = ferramenta
            f.save()
                    
            form = AdicionarAvaliacaoForm()
            messages.success(request,' Dados inseridos com sucesso!!!')
            return redirect('avaliacao:detalhes-ferramenta', id_ferramenta)
        else:
            messages.error(request, 'Erro ao cadastrar !!!')

    template_name = 'adicionar-avaliacao.html'
    context = {

        #'propriedade': Propriedade.objects.filter(usuario=request.user),
        'form': form,
        'f': ferramenta,

    }
    return render(request, template_name, context)


def adicionar_ferramenta (request):    

    form = AdicionarFerramentaForm()

    if request.method == 'POST':
        form = AdicionarFerramentaForm(data = request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
                    
            form = AdicionarFerramentaForm()
            messages.success(request,' Dados inseridos com sucesso!!!')
            return redirect('avaliacao:listar-ferramenta')
        else:
            messages.error(request, 'Erro ao cadastrar !!!')

    template_name = 'adicionar-ferramentas.html'
    context = {

        #'propriedade': Propriedade.objects.filter(usuario=request.user),
        'form': form,

    }
    return render(request, template_name, context)


def editar_ferramenta(request,id_ferramenta):

    try:
            
        template_name = 'editar-ferramenta.html'
            
        ferramenta = Ferramenta.objects.get(id=id_ferramenta)
            
            

        form = AdicionarFerramentaForm(instance=ferramenta)

        if request.method == 'POST':            
            form = AdicionarFerramentaForm(data = request.POST,instance=ferramenta,files=request.FILES)
            if form.is_valid():
                form.save()                
                messages.success(request,' Dados editados com sucesso!')
                return redirect('avaliacao:listar-tabela-ferramenta')
            else:
                messages.error(request, 'Erro ao editar seus dados!')

        return render(request,template_name,{'form':form})
    except:
        raise
        messages.error(request, u" Impossível Editar, contate o administrador do sistema")
        return redirect('avaliacao:listar-tabela-ferramenta')

def editar_categoria(request,id_categoria):

    try:
            
        template_name = 'editar-categoria.html'
            
        categoria = Categoria.objects.get(id=id_categoria)
            
            

        form = AdicionarCategoriaForm(instance=categoria)

        if request.method == 'POST':            
            form = AdicionarCategoriaForm(data = request.POST,instance=categoria)
            if form.is_valid():
                form.save()                
                messages.success(request,' Dados editados com sucesso!')
                return redirect('avaliacao:listar-tabela-categoria')
            else:
                messages.error(request, 'Erro ao editar seus dados!')

        return render(request,template_name,{'form':form})
    except:
        raise
        messages.error(request, u" Impossível Editar, contate o administrador do sistema")
        return redirect('avaliacao:listar-tabela-categoria')



def modal_detalhes_ferramenta (request,id_ferramenta):
       
    template_name = 'modal-detalhes-ferramentas.html'
    

    context = {

     'ferramentas': Ferramenta.objects.get(id=id_ferramenta),

    }
    

    return render(request, template_name,context)


def warning_ferramenta(request,id_ferramenta):

    template_name = 'atencao-ferramenta.html'
    

    context = {
            
            #'planos': planos,
            #'periodo': periodo,
            'f': Ferramenta.objects.get( id=id_ferramenta),
            
     #       'restante': restante,
            }

    return render(request, template_name, context)


@login_required(login_url ='/conta/login/')
def excluir_ferramenta(request,id_ferramenta):   
    
    try:
        f = Ferramenta.objects.get(id=id_ferramenta)

        if f:        
            f.delete()
            messages.success(request,' ferramenta deletada com sucesso')
            return redirect('avaliacao:listar-ferramenta')
        else:
            messages.error(request,' erro ao deletar')
            return redirect('avaliacao:listar-tabela-ferramenta')
    
    except:
        raise

    return redirect('avaliacao:listar-ferramenta')


@login_required(login_url ='/conta/login/')
def listar_tabela_nivel_docente (request):


   
    context = {

        #'categoria': Categoria.objects.all(),
        'nivel_docente':NivelDocente.objects.all(),
        
    }

    template_name = 'listar-tabela-nivel-docente.html'

    return render(request, template_name,context)

@login_required(login_url ='/conta/login/')
def listar_tabela_nivel_dicente (request):


   
    context = {

        #'categoria': Categoria.objects.all(),
        'nivel_dicente':NivelDicente.objects.all(),
        
    }

    template_name = 'listar-tabela-nivel-dicente.html'

    return render(request, template_name,context)


@login_required(login_url ='/conta/login/')
def editar_nivel_dicente(request,id_nivel_dicente):

    try:
            
        template_name = 'editar-nivel-dicente.html'
            
        nivel_dicente = NivelDicente.objects.get(id=id_nivel_dicente)
            
            

        form = AdicionarNivelDicenteForm(instance=nivel_dicente)

        if request.method == 'POST':            
            form = AdicionarNivelDicenteForm(data = request.POST,instance=nivel_dicente)
            if form.is_valid():
                form.save()                
                messages.success(request,' Dados editados com sucesso!')
                return redirect('avaliacao:listar-tabela-nivel-dicente')
            else:
                messages.error(request, 'Erro ao editar seus dados!')

        return render(request,template_name,{'form':form})
    except:
        raise
        messages.error(request, u" Impossível Editar, contate o administrador do sistema")
        return redirect('avaliacao:listar-tabela-nivel-dicente')




@login_required(login_url ='/conta/login/')
def editar_nivel_docente(request,id_nivel_docente):

    try:
            
        template_name = 'editar-nivel-docente.html'
            
        nivel_docente = NivelDocente.objects.get(id=id_nivel_docente)
            
            

        form = AdicionarNivelDocenteForm(instance=nivel_docente)

        if request.method == 'POST':            
            form = AdicionarNivelDocenteForm(data = request.POST,instance=nivel_docente)
            if form.is_valid():
                form.save()                
                messages.success(request,' Dados editados com sucesso!')
                return redirect('avaliacao:listar-tabela-nivel-docente')
            else:
                messages.error(request, 'Erro ao editar seus dados!')

        return render(request,template_name,{'form':form})
    except:
        raise
        messages.error(request, u" Impossível Editar, contate o administrador do sistema")
        return redirect('avaliacao:listar-tabela-nivel-docente')


def warning_nivel_dicente(request,id_nivel_dicente):

    template_name = 'atencao-dicente.html'
    

    context = {
            
            #'planos': planos,
            #'periodo': periodo,
            'n': NivelDicente.objects.get( id=id_nivel_dicente ),
            
     #       'restante': restante,
            }

    return render(request, template_name, context)





@login_required(login_url ='/conta/login/')
def excluir_nivel_dicente(request,id_nivel_dicente):   
    
    try:
        n = NivelDicente.objects.get(id=id_nivel_dicente)

        if n:        
            n.delete()
            messages.success(request,' Nivel deletado com sucesso')
            return redirect('avaliacao:listar-tabela-nivel-dicente')
        else:
            messages.error(request,' erro ao deletar')
            return redirect('avaliacao:listar-tabela-nivel-dicente')
    
    except:
        raise

    return redirect('avaliacao:listar-tabela-nivel-dicente')


def warning_nivel_docente(request,id_nivel_docente):

    template_name = 'atencao-docente.html'
    

    context = {
            
            #'planos': planos,
            #'periodo': periodo,
            'n': NivelDocente.objects.get( id=id_nivel_docente ),
            
     #       'restante': restante,
            }

    return render(request, template_name, context)





@login_required(login_url ='/conta/login/')
def excluir_nivel_docente(request,id_nivel_docente):   
    
    try:
        n = NivelDocente.objects.get(id=id_nivel_docente)

        if n:        
            n.delete()
            messages.success(request,' Nivel deletado com sucesso')
            return redirect('avaliacao:listar-tabela-nivel-docente')
        else:
            messages.error(request,' erro ao deletar')
            return redirect('avaliacao:listar-tabela-nivel-docente')
    
    except:
        raise

    return redirect('avaliacao:listar-tabela-nivel-docente')


def warning_categoria(request,id_categoria):

    template_name = 'atencao-categoria.html'
    

    context = {
            
            #'planos': planos,
            #'periodo': periodo,
            'c': Categoria.objects.get( id=id_categoria),
            
     #       'restante': restante,
            }

    return render(request, template_name, context)





@login_required(login_url ='/conta/login/')
def excluir_categoria(request,id_categoria):   
    
    try:
        c = Categoria.objects.get(id=id_categoria)

        if c:        
            c.delete()
            messages.success(request,' Categoria deletada com sucesso')
            return redirect('avaliacao:listar-tabela-categoria')
        else:
            messages.error(request,' erro ao deletar')
            return redirect('avaliacao:listar-tabela-categoria')
    
    except:
        raise

    return redirect('avaliacao:listar-tabela-categoria')

