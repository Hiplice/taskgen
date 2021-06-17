from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from tests.models import Subject, Topic
from .handler import get_subject_results


@login_required(login_url='/account/auth/', redirect_field_name='')
def show_subjects(request):
    return render(request, 'subjects/subjects.html', {'data': Subject.objects.all()})


@login_required(login_url='/account/auth/', redirect_field_name='')
def show_topics(request):
    subject = Subject.objects.get(id=request.GET.get("subject"))
    return render(request, 'subjects/topics.html', {'data': Topic.objects.filter(subject=subject), 'subject': subject})


@login_required(login_url='/account/auth/', redirect_field_name='')
def show_results(request):
    subject = Subject.objects.get(id=request.GET.get("subject"))
    results = get_subject_results(subject)

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