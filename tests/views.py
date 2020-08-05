from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .generate import TestGenerator


@login_required(login_url='/account/auth/', redirect_field_name='')
def show_tests(request):
    questions = Topic.objects.all()
    return render(request, 'tests/tests.html', {'data': questions})


@login_required(login_url='/account/auth/', redirect_field_name='')
def start_test(request, test_number):
    test = TestGenerator(test_number, 3, 4)

    return render(request, 'tests/questions.html', {'data': test})
