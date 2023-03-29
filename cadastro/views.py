from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CadastroForm, Pesquisaform , Dataform, Pesquisaform_numero, LoginForm
from .models import Cadastro
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from openpyxl import load_workbook
import os

def teste(request):
    return HttpResponse('olá galera')

@login_required
def home(request):
    username = ''
    if request.user.is_authenticated:
        username = request.user
    return render(request,'home.html',{'username':username})

#Inverte a data para Ano - Mes - dia
def corrigi_data(data):

    dia = data[:2]
    mes = data[3:5]
    ano = data[6:10]

    return ano+'-'+mes+'-'+dia

#Salva no banco o formulário se for válido
def salvar_formulario(formulario, dicionario, CadastroForm):
    if formulario.is_valid():
        print("salveiii")
        formulario.save()
        dicionario['susesso'] = True

        formulario = CadastroForm()
    else:
        print('formulario não é válido')
        dicionario['susesso'] = False

#Salva o formulário no Banco
@login_required
def cadastro(request):
    dicionario = {}
    dicionario['editar'] = False
    dicionario['susesso'] = None
    dicionario ['salvar'] = True
    dicionario['editar'] = False
    dicionario['id'] = 0
    if request.method == 'POST':

        data_do_processo = request.POST.get('data_do_processo')

        post_data = request.POST.copy()

        print(post_data)

        post_data['data_do_processo'] = corrigi_data(data_do_processo)

        data_do_recebimento = request.POST.get('data_do_recebimento')

        post_data['data_do_recebimento'] = corrigi_data(data_do_recebimento)

        formulario = CadastroForm(post_data)

        salvar_formulario(formulario, dicionario, CadastroForm)

        formulario = CadastroForm()

    else:
        formulario = CadastroForm()
    dicionario['form'] = formulario
    dicionario['username'] = request.user

    return render(request, 'cadastro.html', dicionario)

@login_required
def pesquisa(request):
    return render(request, 'base_pesquisa.html')

#Pesquisa por data de inicio e fim
@login_required
def novapesquisa(request):
    if request.method == 'GET':
        form = Dataform
        context = {'form': form}
        return render(request, 'base_pesquisa.html', context)

    if (request.method == 'POST'):

        form = Dataform(request.POST)

        if form.is_valid():

            data_inicial = form.data['data_inicio']
            data_final = form.data['data_fim']

            results = Cadastro.objects.filter(Q(data_do_recebimento__gte=corrigi_data(data_inicial)) & Q(
                    data_do_recebimento__lte=corrigi_data(data_final)))

            context = {'form': form, 'results': results}
            context['username'] = request.user
            return render(request, 'base_pesquisa.html', context)

#Pesquisa por nome
@login_required
def pesquisa_string(request):
    if request.method == 'GET':

        form = Pesquisaform
        context = {'form':form}
        return render(request, 'base_pesquisa.html', context)

    if (request.method == 'POST'):

        form = Pesquisaform(request.POST)
        query = form.data['query']

        if form.is_valid():

            results = Cadastro.objects.filter(requerente__icontains=query)

            context = {'form': form, 'results': results}
            context['username'] = request.user
            return render(request, 'base_pesquisa.html', context)

#Pesquisa por número de processo
@login_required
def pesquisa_numero(request):
    if request.method == 'GET':

        form = Pesquisaform_numero
        context = {'form':form}
        return render(request, 'base_pesquisa.html', context)

    if (request.method == 'POST'):

        form = Pesquisaform(request.POST)
        query = form.data['query']

        if form.is_valid():

            results = Cadastro.objects.filter(numero_do_processo__icontains=query)

            context = {'form': form, 'results': results}
            context['username'] = request.user
            return render(request, 'base_pesquisa.html', context)


@login_required
def editar_cadastro(request, variavel):
        dicionario = {}
        dicionario['susesso'] = None
        dicionario['editar'] = True
        dicionario['salvar'] = True

        objeto = Cadastro.objects.get(id=variavel)

        form = CadastroForm(instance=objeto)
        dicionario['form'] = form

        id = request.POST.get('data_inicios')

        dicionario['id'] = variavel

        if request.method == 'GET':

            return render(request, 'cadastro.html', dicionario)
        else:

            data_do_processo = request.POST.get('data_do_processo')

            post_data = request.POST.copy()

            post_data['data_do_processo'] = corrigi_data(data_do_processo)

            data_do_recebimento = request.POST.get('data_do_recebimento')

            post_data['data_do_recebimento'] = corrigi_data(data_do_recebimento)

            formulario = CadastroForm(post_data, instance=objeto)

            salvar_formulario(formulario, dicionario, CadastroForm)

            dicionario['form'] =  CadastroForm()

            dicionario['username'] = request.user
            return render(request, 'cadastro.html', dicionario)

@login_required
def excluir(request, variavel):
    print('entrei na excluir'+str(variavel))

    objeto = Cadastro.objects.get(id=variavel)

    objeto.delete()
    return render(request, 'cadastro.html',{'alerta':True})

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        print(request.user)

        user = authenticate(username=username, password=password)

        if request.user.is_authenticated:
            return redirect('/registro/home')
        else:
            sucesso = None
            if user is not None:
                sucesso = False
                auth_login(request, user)
                print(request.user)
                return redirect('/registro/home')
            else:
                sucesso = True
                print("Usuário inválido")
                # Exibir uma mensagem de erro se a autenticação falhar
                return render(request, 'login.html', {'form': form, 'sucesso':sucesso})
    else:
        # Se for um pedido GET, exibir o formulário de login vazio
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    print('tentei logout')
    return redirect('/registro/login')

@login_required
def upload(request):
    result = None
    if (request.method == 'GET'):
        return render(request, 'upload.html')
    elif request.method == 'POST':

        # Obtém o arquivo enviado através da solicitação POST
        file = request.FILES['xlsx_file']

        valid_extensions = ['.xls', '.xlsx']
        ext = os.path.splitext(file.name)[1]
        if not ext.lower() in valid_extensions:
            result = False
        else:
            result = True

            # Carrega o arquivo com a biblioteca openpyxl
            workbook = load_workbook(file)

            # Acesse as folhas do arquivo e faça algo com os dados
            sheet = workbook.active

            for row in sheet.iter_rows(values_only=True):
                print(row)
                print(type(row))

            formulario = Cadastro(requerente='teste2',
                assunto='Rodrigo',
                numero_do_processo='2342424',
                ano=2023,
                data_do_processo='2022-01-02',
                data_do_recebimento='2022-02-02',
                responsavel='Prefeitura',
                status='Concluído')

            formulario.save()
            # Renderiza uma resposta com uma mensagem de sucesso
            return render(request, 'upload.html',{'result':result})
    return render(request, 'upload.html', {'result': result})