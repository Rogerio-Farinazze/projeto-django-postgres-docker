from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
def index(request):
    message_negative = "Acesso Negado!"
    #Checked Login
    if request.method == "POST": 
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        #Authenticate
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request,user)
            messages.success(request, "Acesso concedido com sucesso!")
            return redirect('app:index')
        else:
            messages.warning(request, message_negative)
            return redirect('app:index')
    else:
        return render(request, 'index.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Sessão Encerrada com Sucesso!")
    return redirect('app:index')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Seu registro foi realizado com sucesso!")
			return redirect('app:index')
	else:
		form = SignUpForm()
		return render(request, 'base/register.html', {'form':form})

	return render(request, 'base/register.html', {'form':form})

