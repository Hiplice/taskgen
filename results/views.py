from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from tests.models import Subject, Topic, Test, QuestionsData
from .handler import get_subject_results
from account.models import User, StudyGroup


@login_required(login_url='/account/auth/', redirect_field_name='')
def show_subjects(request):
    return render(request, 'subjects/subjects.html', {'data': Subject.objects.all()})


@login_required(login_url='/account/auth/', redirect_field_name='')
def show_topics(request):
    subject = Subject.objects.get(id=request.GET.get("subject"))
    return render(request, 'subjects/topics.html', {'data': Topic.objects.filter(subject=subject), 'subject': subject})


@login_required(login_url='/account/auth/', redirect_field_name='')
def show_groups(request):
    topic = Topic.objects.get(id=request.GET.get("topic"))
    groups = []
    user_groups = Test.objects.filter(topic_id=topic)
    for group in user_groups:
        if group.user.study_group not in groups:
            groups.append(StudyGroup.objects.get(id=group.user.study_group.id))

    return render(request, 'subjects/groups.html', {'data': groups, 'topic': topic})


@login_required(login_url='/account/auth/', redirect_field_name='')
def show_res(request):
    req = request.GET.get("topic")
    id_base = req.split("/?")
    topic_id = id_base[0]
    topic = Topic.objects.get(id=topic_id)
    id_base[1] = id_base[1].replace("groups=", "")
    group_id = id_base[1]
    tests = Test.objects.filter(topic=topic, user__study_group_id=group_id)
    tests.exclude(last_question=None)
    total_questions = tests.filter().first().total_questions
    total_questions = range(1, total_questions+1)
    questions_data = []
    for test_id in tests:
        questions_data.append(QuestionsData.objects.filter(test=test_id))

    final_count = []
    for i in total_questions:
        summa = 0
        for test_id in tests:
            temp = QuestionsData.objects.filter(test_id=test_id.id)
            summa += temp.get(counter=i).point
        final_count.append(summa)

    final_count.append(sum(final_count))
    return render(request, 'subjects/res.html', {'topic': topic, 'data': questions_data,
                                                 'tests': tests,
                                                 'tq': total_questions,
                                                 'tqc': len(total_questions),
                                                 'fc': final_count})


@login_required(login_url='/account/auth/', redirect_field_name='')
def show_results(request):
    subject = Subject.objects.get(id=request.GET.get("subject"))
    user_status = User.objects.get(id=request.user.id).study_group.id
    results = get_subject_results(subject, user_status)
    if request.GET.get("search"):
        new_res = []
        keyword = request.GET.get("search")
        for i in results:
            if i.name.lower().count(keyword.lower()) or i.surname.lower().count(keyword.lower()) or i.group.lower().count(keyword.lower()):
                new_res.append(i)
        results = new_res

    return render(request, 'subjects/results.html', {'data': results, 'subject': subject, 'topics': [i for i in range(1, len(subject.topic_set.all()) + 1)]})


@login_required(login_url='/account/auth/', redirect_field_name='')
def add_subject(request):
    Subject(name=request.POST.get("name")).save()
    return redirect(to='/subjects/')


@login_required(login_url='/account/auth/', redirect_field_name='')
def remove_subject(request):
    Subject.objects.get(id=request.GET.get('subject')).delete()
    return redirect(to='/subjects/')


@login_required(login_url='/account/auth/', redirect_field_name='')
def add_topic(request):
    Topic(subject_id=request.GET.get('subject'), name=request.POST.get("name")).save()
    return redirect(to=f'/subjects/topics/?subject={request.GET.get("subject")}')


@login_required(login_url='/account/auth/', redirect_field_name='')
def remove_topic(request):
    subject_id = Subject.objects.get(topic=request.GET.get("topic")).id
    Topic.objects.get(id=request.GET.get('topic')).delete()
    return redirect(to=f'/subjects/topics/?subject={subject_id}')