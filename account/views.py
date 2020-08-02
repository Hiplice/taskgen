from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import *


form_fields = {
    'auth': ['login', 'password'],
    'register': ['username', 'email', 'password', 'name', 'surname'],
}


def auth(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Авторизация прошла успешно.')
                else:
                    return HttpResponse('Аккаунт был удалён.')
            else:
                return HttpResponse('Неверно введён логин/пароль.')

    else:
        form = AuthForm()
    return render(request, 'account/auth.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return HttpResponse("{}/{}".format(data['first_name'], data['second_name']))

        return HttpResponse("Регистрация недоступна")
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})

