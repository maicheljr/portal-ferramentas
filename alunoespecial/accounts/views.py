from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import *   
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from datetime import *

from .models import Usuario




def loginUser (request):

    

    template_name = 'login.html'

    logout(request)
    
    if request.POST:
        username = request.POST['usuario']
        password = request.POST['password']

        user= authenticate(username = username, password= password) 
               
        if user is not None:
            


            if user.is_active:

                login(request,user) 

                if user.usuario.nivel_acesso == 'administrador' :                    

                    return redirect('avaliacao:listar-tabela-ferramenta')
                
                if user.usuario.nivel_acesso == 'professor' :                    

                    return redirect('avaliacao:listar-tabela-ferramenta')                
                                                
                else:
                    return redirect('avaliacao:listar-ferramenta')
                
            else:
                messages.error(request,'usuario inválido')   
                

        else:
            messages.error(request,'Usuário não encontrado, faça seu cadastro!')
            return redirect('accounts:adicionar-usuario')
            #criar m
            #aqui se nao deu joga pra mesma tela pesquesar messages django
            #inserir tags de erro no  template login.html para tratar
        #user_name = request.POST.get()

    return render(request, template_name)

def logoutUser(request):

    logout(request)

    return redirect('accounts:loginUser')


def adicionar_usuario (request):

    template_name = 'adicionar-usuario.html' 
    form = AdicionarUsuarioForm()  

    if request.method == 'POST':
        form = AdicionarUsuarioForm(data = request.POST, files=request.FILES)
        if form.is_valid():
            f = form.save()
            f.password = make_password(f.password)
            f.save()
            form = AdicionarUsuarioForm()
            messages.success(request,' Usuário inserido com sucesso, você já pode acessar o sistema!!!')
            return redirect('accounts:loginUser')            
        else:
            messages.error(request, 'Erro ao cadastrar !!!')
    return render(request,template_name,{'form':form})





    

    return render(request, template_name)

def adicionar_usuario_interno (request):

    template_name = 'adicionar-usuario-interno.html' 
    form = AdicionarInternoForm() 

    if request.method == 'POST':
        form = AdicionarInternoForm(data = request.POST, files=request.FILES)
        if form.is_valid():
            f = form.save()
            f.password = make_password(f.password)
            f.save()
            form = AdicionarInternoForm()
            messages.success(request,' Usuário inserido com sucesso, você já pode acessar o sistema!!!')
            return redirect('accounts:adicionar-usuario-interno')            
        else:
            messages.error(request, 'Erro ao cadastrar !!!')
    return render(request,template_name,{'form':form})
    

    return render(request, template_name)

@login_required(login_url ='/conta/login/')
def editar_usuario_interno (request,id_usuario):

    try:
            
        template_name = 'editar-usuario-interno.html'
            
        usuario = Usuario.objects.get(id=id_usuario)
            
            

        form = AdicionarInternoForm(instance=usuario)

        if request.method == 'POST':            
            form = AdicionarInternoForm(data = request.POST,instance=usuario,files=request.FILES)
            if form.is_valid():
                f = form.save()
                f.password = make_password(f.password)
                f.save()               
                messages.success(request,' Dados editados com sucesso!')
                return redirect('accounts:listar-usuarios')
            else:
                messages.error(request, 'Erro ao editar seus dados!')

        return render(request,template_name,{'form':form})
    except:
        raise
        messages.error(request, u" Impossível Editar, contate o administrador do sistema")
        return redirect('accounts:listar-usuarios')



def listar_usuarios (request):
   
    context = {

        'usuario': Usuario.objects.all(),
        #'ferramentas':Ferramenta.objects.all(),
        
    }

    template_name = 'listar-usuarios.html'

    return render(request, template_name,context)


def profile(request,id_usuario):
    
    template_name = 'profile-usuario.html'
    usr = Usuario.objects.get( id=id_usuario ) 

    context = {
            
            #'planos': planos,
            #'periodo': periodo,
            'usr': usr,
            
     #       'restante': restante,
            }

    return render(request, template_name,context)


def warning(request,id_usuario):

    template_name = 'atencao.html'
    usr = Usuario.objects.get( id=id_usuario )

    context = {
            
            #'planos': planos,
            #'periodo': periodo,
            'usr': usr,
            
     #       'restante': restante,
            }

    return render(request, template_name, context)


@login_required(login_url ='/conta/login/')
def excluir_usuario(request,id_usuario):   
    
    try:
        u = Usuario.objects.get(id=id_usuario)

        if u:        
            u.delete()
            messages.success(request,'<b>'+' o usuário foi deletado com sucesso'+'</b>')
            return redirect('accounts:listar-usuarios')
        else:
            messages.error(request,' erro ao deletar !!')
            return redirect('accounts:listar-usuarios')
    
    except:
        raise

    return redirect('accounts:listar-usuarios')