from django.db import models


class Question(models.Model):
    test_number = models.PositiveIntegerField()
    text = models.TextField()


def __str__(self):
    return self.title
