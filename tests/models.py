from django.db import models
from account.models import User


class Topic(models.Model):
    name = models.CharField(max_length=50)


class Question(models.Model):
    test_number = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()


class Test(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.TextField()
    answers = models.TextField()


def __str__(self):
    return self.title
