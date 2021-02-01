from django.db import models
from account.models import User
from django.utils import timezone


class Subject(models.Model):
    name = models.CharField(max_length=50)


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Pattern(models.Model):
    topic_number = models.ForeignKey(Topic, on_delete=models.CASCADE)
    difficulty = models.PositiveIntegerField()
    text = models.TextField()


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    difficulty = models.PositiveIntegerField()
    questions = models.TextField()
    answers = models.TextField()
    correct_answers = models.TextField()
    chosen_answers = models.TextField()
    start_time = models.TimeField(default=timezone.now)


class TestData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    attempts = models.PositiveSmallIntegerField()
    best_result = models.PositiveSmallIntegerField()


def __str__(self):
    return self.title
