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
        answer = handler.check_answer(request.user, request.POST['answer'])
        test = Test.objects.get(id=request.user.active_test)
        if test.question_count < test.total_questions:
            if test.topic.id == 13:
                handler.create_direct_question(test)
            else:
                handler.create_question(test)
        else:
            handler.update_result(request.user)
        result = HttpResponse(answer)
    elif request.user.active_test:
        test, question = handler.get_test_data(request.user.active_test)
        result = render(request, 'tests/question.html', {'question': question, 'test': test, "progress": 100 * test.question_count / test.total_questions})
    elif request.GET.get('topic'):
        topic = request.GET.get("topic")
        if topic == '13':
            question, test = handler.create_direct_test(request.user, topic)
            result = render(request, 'tests/question.html', {'question': question, 'test': test,
                                                             "progress": 100 * test.question_count / test.total_questions})
        else:
            question, test = handler.create_test(request.user, topic)
            result = render(request, 'tests/question.html', {'question': question, 'test': test, "progress": 100 * test.question_count / test.total_questions})
    else:
        result = redirect('/tests/')

    return result