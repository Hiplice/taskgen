from django.shortcuts import render
from django.http import HttpResponse


def patterns(request):
    return HttpResponse('Вот тут управление шаблонами короче')


def start_test(request):
    return HttpResponse('Тут тест надо проходиц')
