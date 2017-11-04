from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.forms import *
from .models import *
from django import forms
from alunoespecial.avaliacao.models import *
from django.contrib.admin.widgets import AdminDateWidget 
from django.core.urlresolvers import reverse


class AdicionarCategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome','descricao']
        exclude = ['created_at', 'upload_at']    

    def __init__(self, *args, **kwargs):

        super(AdicionarCategoriaForm, self).__init__(*args, **kwargs)    
        #self.user = user
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['descricao'].widget.attrs={ 
           
           'rows': '5',
            
            }

        self.fields['descricao'].widget.attrs['class'] = 'form-control'

class AdicionarNivelDicenteForm(ModelForm):
    class Meta:
        model = NivelDicente
        fields = ['nome','descricao']
        exclude = ['created_at', 'upload_at']    

    def __init__(self, *args, **kwargs):

        super(AdicionarNivelDicenteForm, self).__init__(*args, **kwargs)    
        #self.user = user
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['descricao'].widget.attrs={ 
           
           'rows': '5',
            
            }

        self.fields['descricao'].widget.attrs['class'] = 'form-control'

class AdicionarNivelDocenteForm(ModelForm):
    class Meta:
        model = NivelDocente
        fields = ['nome','descricao']
        exclude = ['created_at', 'upload_at']    

    def __init__(self, *args, **kwargs):

        super(AdicionarNivelDocenteForm, self).__init__(*args, **kwargs)    
        #self.user = user
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['descricao'].widget.attrs={ 
           
           'rows': '5',
            
            }

        self.fields['descricao'].widget.attrs['class'] = 'form-control'

class AdicionarAvaliacaoForm(ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['avaliacao_pro','avaliacao_contra','recomendacoes']
        exclude = ['created_at', 'upload_at']    

    def __init__(self, *args, **kwargs):

        super(AdicionarAvaliacaoForm, self).__init__(*args, **kwargs)    
        #self.user = user
        
        self.fields['avaliacao_pro'].widget.attrs={ 
           
           'rows': '5',
            
            }

        self.fields['avaliacao_contra'].widget.attrs={ 
           
           'rows': '5',
            
            }

        self.fields['recomendacoes'].widget.attrs={ 
           
           'rows': '5',
            
            }

        self.fields['avaliacao_pro'].widget.attrs['class'] = 'form-control'
        self.fields['avaliacao_contra'].widget.attrs['class'] = 'form-control'
        self.fields['recomendacoes'].widget.attrs['class'] = 'form-control'

class AdicionarFerramentaForm(ModelForm):
    class Meta:
        model = Ferramenta     
        
        fields = ['nome','categoria','nivel_professor','nivel_aluno','descricao','requisitos_sistema','indicacao_pedagogica','link_download','imagem']
        #fields = ['nome','categoria','descricao','requisitos_sistema','indicacao_pedagogica','link_download','imagem']
        exclude = ['created_at', 'upload_at']    

    def __init__(self, *args, **kwargs):

        super(AdicionarFerramentaForm, self).__init__(*args, **kwargs)    
        #self.user = user
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['link_download'].widget.attrs['class'] = 'form-control'
        self.fields['categoria'].queryset = Categoria.objects.all().order_by('nome')
        
        
        
        self.fields['categoria'].widget.attrs={ 
            'class': 'selectpicker', 
            'data-style': 'btn btn-rose btn-round',             
            'data-size':'7',

            } 


        
        self.fields['nivel_professor'].widget.attrs={ 
            'class': 'selectpicker', 
            'data-style': 'btn btn-rose btn-round',             
            'data-size':'7',
            
            } 

        self.fields['nivel_aluno'].widget.attrs={ 
            'class': 'selectpicker', 
            'data-style': 'btn btn-rose btn-round',             
            'data-size':'7',
            
            }
        
        self.fields['requisitos_sistema'].widget.attrs={ 
           
           'rows': '5',
            
            }

        self.fields['indicacao_pedagogica'].widget.attrs={ 
           
           'rows': '5',
            
            }

        self.fields['descricao'].widget.attrs={ 
           
           'rows': '5',
            
            }

        

        self.fields['requisitos_sistema'].widget.attrs['class'] = 'form-control'
        self.fields['indicacao_pedagogica'].widget.attrs['class'] = 'form-control'
        self.fields['descricao'].widget.attrs['class'] = 'form-control'
        #self.fields[''].widget.attrs['class'] = 'form-control'
        self.fields['imagem'].widget.attrs={ 
           
           'data-provides':'fileinput',
           'class':'btn btn-rose btn-round btn-file ',
           
           

            
            }
        
                                                        
        
    


