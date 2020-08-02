from django.shortcuts import render
from .forms import *
from django.http import HttpResponse


form_fields = {
    'auth': ['login', 'password'],
    'register': ['username', 'email', 'password', 'name', 'surname'],
}


def auth(request):
    if request.method == 'POST':
        data = get_post_data(form_fields['auth'], request)
        return HttpResponse("<h2>Hello, {0}</h2>".format(data['login']))
    else:
        auth_form = AuthForm()
        return render(request, 'account/auth.html', {'form': auth_form})


def register(request):
    if request.method == 'POST':
        data = get_post_data(form_fields['register'], request)
        return HttpResponse("<h2>Hello, {0} {1}</h2>".format(data['name'], data['surname']))
    else:
        register_form = RegisterForm()
        return render(request, 'account/register.html', {'form': register_form})

