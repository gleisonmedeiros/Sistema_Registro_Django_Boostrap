from django import forms
from django.forms import ClearableFileInput

from .models import Cadastro
from django.contrib.auth.forms import AuthenticationForm


class CadastroForm(forms.ModelForm):
    #imagens = forms.ImageField(required=False,widget=ClearableFileInput(attrs={'multiple': True,'class':'form-control w-50'}))
    class Meta:
        #imagens = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True,'class':'form-control','aria-describedby':'inputGroupFileAddon04','aria-label':'Upload'}), required=False)
        model = Cadastro
        fields = ['requerente',
                  'assunto',
                  'numero_do_processo',
                  'ano',
                  'data_do_processo',
                  'data_do_recebimento',
                  'responsavel',
                  'status',
                  'destino']
        
       # images = forms.FileInput()

        css1 = forms.TextInput(attrs={
            'type': 'text', 'class': 'form-control w-50'})

        dicionario = {}

        for i in fields:
            dicionario[i] = css1

        #fields.append('imagens')

        css1 = forms.TextInput(attrs={
            'type': 'text', 'class': 'form-control w-50'})

        formato_data = \
            forms.DateInput(attrs={'type': 'text','class':'data form-control w-25','required': 'False','value': ''})

        dicionario['data_do_processo'] = formato_data
        dicionario['data_do_recebimento'] = formato_data
        #dicionario['imagens'] = forms.FileInput(attrs={'multiple': True,'class':'form-control','required ':False})

        widgets = dicionario


class Cadastro_imagem_Form(forms.ModelForm):
    imagens = forms.ImageField(required=False,
                               widget=ClearableFileInput(attrs={'multiple': True, 'class': 'form-control w-50'}))

    class Meta:
        # imagens = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True,'class':'form-control','aria-describedby':'inputGroupFileAddon04','aria-label':'Upload'}), required=False)
        model = Cadastro
        fields = ['requerente',
                  'assunto',
                  'numero_do_processo',
                  'ano',
                  'data_do_processo',
                  'data_do_recebimento',
                  'responsavel',
                  'status',
                  'destino']

        # images = forms.FileInput()

        css1 = forms.TextInput(attrs={
            'type': 'hidden', 'class': 'form-control w-50'})

        dicionario = {}

        for i in fields:
            dicionario[i] = css1

        fields.append('imagens')

        css1 = forms.TextInput(attrs={
            'type': 'text', 'class': 'form-control w-50'})

        formato_data = \
            forms.DateInput(attrs={'type': 'hidden', 'class': 'data form-control w-25', 'required': 'False', 'value': ''})

        dicionario['data_do_processo'] = formato_data
        dicionario['data_do_recebimento'] = formato_data
        # dicionario['imagens'] = forms.FileInput(attrs={'multiple': True,'class':'form-control','required ':False})

        widgets = dicionario

class Pesquisaform(forms.Form):
    query = forms.CharField(label='Digite o nome:',
                            required=False,
                            max_length=100,
                            widget=forms.TextInput(attrs={
                                'type': 'text',
                                'class': 'form-control w-50',
                                }))


class Pesquisaform_numero(forms.Form):
    query = forms.CharField(label='Digite o número:',
                            max_length=100,
                            widget=forms.TextInput(attrs={
                                'type': 'text',
                                'class': 'form-control w-50'}))


class Dataform(forms.Form):
    data_inicio = forms.DateField(
        label='Data Início', widget=forms.TextInput(
            attrs={'type': 'text', 'class': 'form-control w-25 data'}))
    data_fim = forms.DateField(
        label='Data Fim', widget=forms.TextInput(
            attrs={'type': 'text', 'class': 'form-control w-25 data'}))


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuário', widget=forms.TextInput(
            attrs={'type': 'text', 'class': 'form-control'}))
    password = forms.CharField(
        label='Senha', widget=forms.PasswordInput(
            attrs={'type': 'password', 'class': 'form-control'}))



   

