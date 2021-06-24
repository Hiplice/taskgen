from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from . import handler
from django.http import HttpResponse


@login_required(login_url='/account/auth/', redirect_field_name='')
def redirect_from_root(request):
    return redirect(to='/tests/')


@login_required(login_url='/account/auth/', redirect_field_name='')
def show_tests(request):
    tests_information = handler.get_subject_information(request)

    return render(request, 'tests/tests.html', {'data': tests_information})


@login_required(login_url='/account/auth/', redirect_field_name='')
def start_test(request):
    if request.method == 'POST':
        result = HttpResponse("Пока не фурычит")
    else:
        topic = request.GET.get("topic")

        result = render(request, 'tests/question.html')
    return result