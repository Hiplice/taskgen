from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .generate import TestGenerator
from . import handler
from django.http import HttpResponse


@login_required(login_url='/account/auth/', redirect_field_name='')
def redirect_from_root(request):
    return redirect(to='/tests/')


@login_required(login_url='/account/auth/', redirect_field_name='')
def show_tests(request):
    questions = Topic.objects.all()
    return render(request, 'tests/tests.html', {'data': questions})


@login_required(login_url='/account/auth/', redirect_field_name='')
def start_test(request, test_number):
    if request.method == 'POST':
        accuracy = handler.compare_result(request)
        result = HttpResponse(accuracy)
    else:
        test = TestGenerator(test_number, 10, 4, 0)
        handler.create_test(test, request)
        result = render(request, 'tests/questions.html', {'data': test})

    return result


@login_required(login_url='/account/auth/', redirect_field_name='')
def add_test(request):
    return render(request, 'tests/addtest.html')