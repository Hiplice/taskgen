from django.db import models
from account.models import User
from tests.models import Topic


class TopicPassing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)

    difficulty = models.PositiveIntegerField()
    total_points = models.PositiveIntegerField()
    max_points = models.PositiveIntegerField()