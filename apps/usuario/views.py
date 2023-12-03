from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from apps.usuario.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():   

            login = form['login'].value()
            senha = form['senha'].value()
        
            usuario = auth.authenticate(
                request,
                username = login,
                password = senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, "Login efetuado com sucesso!")
                return redirect('index')
            else:
                messages.error(request, "Erro ao realizar o login!")
                return redirect('login')
        
    return render(request, 'usuario/login.html', {"form":form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():            

            nome = form['nome'].value()
            email = form['email'].value()
            senha = form['senha'].value()

            if User.objects.filter(username = nome).exists():
                messages.error(request, "Usuário já existe!")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')

    return render(request, 'usuario/cadastro.html', {"form":form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect('login')    
    