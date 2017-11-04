from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.forms import *
from .models import *
from django import forms
from alunoespecial.avaliacao.models import *
from django.contrib.admin.widgets import AdminDateWidget 
from django.core.urlresolvers import reverse




class AdicionarUsuarioForm(ModelForm):
    class Meta:
        model = Usuario     
        # o campo esperiência está escrito errado e fique com preguiça de fazer um migrate no banco, kkk!!!
        fields = ['username','email','password','endereco','profissao','experiencia','uf','cidade','image']
        #fields = ['nome','categoria','descricao','requisitos_sistema','indicacao_pedagogica','link_download','imagem']
        exclude = ['created_at', 'upload_at']    

    def __init__(self, *args, **kwargs):

        super(AdicionarUsuarioForm, self).__init__(*args, **kwargs)    
        #self.user = user
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['endereco'].widget.attrs['class'] = 'form-control'
        self.fields['profissao'].widget.attrs['class'] = 'form-control'

        self.fields['uf'].widget.attrs={ 
            'class': 'selectpicker', 
            'data-style': 'btn btn-rose btn-round',             
            'data-size':'7',

            } 
        
        
        self.fields['experiencia'].widget.attrs={ 
           
           'rows': '5',
            
            }

        self.fields['username'].widget.attrs={ 
                   
           'placeholder': 'digite um usuario'
                    
            }
        self.fields['password'] = forms.CharField(widget=forms.PasswordInput)
        self.fields['password'].label = "Senha"

        self.fields['image'].widget.attrs={ 
           
           'data-provides':'fileinput',
           'class':'btn btn-rose btn-round btn-file ',
           
           

            
            }
        
        self.fields['uf'].label = "Estado"
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['experiencia'].widget.attrs['class'] = 'form-control'
        self.fields['cidade'].widget.attrs['class'] = 'form-control'

        
class AdicionarInternoForm(ModelForm):
        class Meta:
            model = Usuario     
            # o campo esperiência está escrito errado e fique com preguiça de fazer um migrate no banco, kkk!!!
            fields = ['username','email','password','nivel_acesso','endereco','profissao','experiencia','uf','cidade','image', ]
            #fields = ['nome','categoria','descricao','requisitos_sistema','indicacao_pedagogica','link_download','imagem']
            exclude = ['created_at', 'upload_at']    

        def __init__(self, *args, **kwargs):

            super(AdicionarInternoForm, self).__init__(*args, **kwargs)    
            #self.user = user
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['endereco'].widget.attrs['class'] = 'form-control'
            self.fields['profissao'].widget.attrs['class'] = 'form-control'

            self.fields['uf'].widget.attrs={ 
                'class': 'selectpicker', 
                'data-style': 'btn btn-rose btn-round',             
                'data-size':'7',

                } 

            self.fields['nivel_acesso'].widget.attrs={ 
                'class': 'selectpicker', 
                'data-style': 'btn btn-rose btn-round',             
                'data-size':'7',

                } 
            
            
            self.fields['experiencia'].widget.attrs={ 
               
               'rows': '5',
                
                }

            self.fields['password'] = forms.CharField(widget=forms.PasswordInput)
            self.fields['password'].label = "Senha"

            self.fields['image'].widget.attrs={ 
               
               'data-provides':'fileinput',
               'class':'btn btn-rose btn-round btn-file ',
               
               

                
                }
            
            self.fields['uf'].label = "Estado"
            self.fields['nivel_acesso'].label = "Nível de acesso"
            self.fields['password'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['experiencia'].widget.attrs['class'] = 'form-control'
            self.fields['cidade'].widget.attrs['class'] = 'form-control'    

            
        


