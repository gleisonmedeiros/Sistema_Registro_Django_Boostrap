from django import forms
from .models import Cadastro
from django.contrib.auth.forms import AuthenticationForm

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['requerente', 'assunto', 'numero_do_processo', 'ano', 'data_do_processo','data_do_recebimento','responsavel','status']

        css1 = forms.TextInput(attrs={'type':'text','class':'form-control w-50'})

        dicionario = {}

        for i in fields:
            dicionario[i] = css1

        formato_data = forms.DateInput(attrs={'type':'text','class':'data form-control w-25'})

        dicionario['data_do_processo'] = formato_data
        dicionario['data_do_recebimento'] = formato_data

        widgets = dicionario


class Pesquisaform(forms.Form):
    query = forms.CharField(label='Digite o nome:',
                            max_length=100,
                            widget=forms.TextInput(attrs={'type':'text','class':'form-control w-50'}))

class Pesquisaform_numero(forms.Form):
    query = forms.CharField(label='Digite o número:',
                            max_length=100,
                            widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control w-50'}))


class Dataform(forms.Form):
    data_inicio = forms.DateField(label='Data Início',
                            widget=forms.TextInput(attrs={'type':'text','class':'form-control w-25 data'}))
    data_fim = forms.DateField(label='Data Fim',
                            widget=forms.TextInput(attrs={'type':'text','class':'form-control w-25 data'}))


class LoginForm(AuthenticationForm):
    
    username = forms.CharField(label='Usuário',
                               widget=forms.TextInput(attrs={'type':'text','class':'form-control'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'type':'password','class':'form-control'}))


    pass