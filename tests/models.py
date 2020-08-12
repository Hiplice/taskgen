from django.db import models
from account.models import User


class Subject(models.Model):
    name = models.CharField(max_length=50)


class Topic(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Pattern(models.Model):
    topic_number = models.ForeignKey(Topic, on_delete=models.CASCADE)
    difficulty = models.PositiveIntegerField()
    text = models.TextField()


class Test(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.TextField()
    answers = models.TextField()


def __str__(self):
    return self.title
