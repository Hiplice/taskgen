from django.shortcuts import render
from django.http import HttpResponse


def auth(request):
    return render(request, 'account/auth.html')


def register(request):
    return render(request, 'account/register.html')
