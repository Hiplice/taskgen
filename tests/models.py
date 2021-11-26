from django.db import models
from account.models import User
from django.utils import timezone


class Subject(models.Model):
    name = models.CharField(max_length=50)


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Pattern(models.Model):
    levels = (
        (1, 'Первый уровень'),
        (2, 'Второй уровень'),
        (3, 'Третий уровень'),
    )
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    difficult = models.IntegerField(default=1, choices=levels)
    heading = models.CharField(max_length=128)
    question_body = models.TextField(null=True)
    expression = models.TextField()
    generate_from = models.IntegerField()
    generate_to = models.IntegerField()
    answer_from = models.IntegerField()
    answer_to = models.IntegerField()


class Question(models.Model):
    difficulty = models.IntegerField()
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


class QuestionsData(models.Model):
    difficulty = models.IntegerField(default=1)
    pattern = models.ForeignKey(Pattern, default=0, on_delete=models.CASCADE)
    correct_answer = models.IntegerField()
    heading = models.CharField(max_length=128)
    body = models.TextField()
    answers = models.TextField()
    test = models.ForeignKey(Test, default=0, on_delete=models.CASCADE)
    user_answer = models.IntegerField(default=0)
    counter = models.IntegerField(default=1)
    point = models.IntegerField(default=0)
    max_point=models.IntegerField(default=0)


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
