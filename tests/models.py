from django.db import models
from account.models import User
from django.utils import timezone


class Subject(models.Model):
    name = models.CharField(max_length=50)


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Pattern(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    difficult = models.BooleanField(default=False)
    heading = models.CharField(max_length=128)
    question_body = models.TextField(null=True)
    expression = models.TextField()
    generate_from = models.IntegerField()
    generate_to = models.IntegerField()
    answer_from = models.IntegerField()
    answer_to = models.IntegerField()


class Question(models.Model):
    parent_pattern = models.ForeignKey(Pattern, on_delete=models.SET_NULL, null=True)
    correct_answer = models.IntegerField()
    heading = models.CharField(max_length=128)
    body = models.TextField()
    answers = models.TextField()


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    streak = models.PositiveSmallIntegerField(default=0)
    last_question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    question_count = models.PositiveSmallIntegerField(default=1)
    total_questions = models.PositiveSmallIntegerField(default=10)
    points = models.PositiveSmallIntegerField(default=0)
    start_time = models.TimeField(default=timezone.now)


class TestData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    attempts = models.PositiveSmallIntegerField()
    best_result = models.PositiveSmallIntegerField()


class SubjectPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


def __str__(self):
    return self.title
