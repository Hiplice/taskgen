from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tests.models import Subject


@login_required(login_url='/account/auth/', redirect_field_name='')
def show_subjects(request):

    return render(request, 'subjects/subjects.html', {'data': Subject.objects.all()})
