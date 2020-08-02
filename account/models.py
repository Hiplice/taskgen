from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)

    name = models.CharField(max_length=20, null=False)
    surname = models.CharField(max_length=30, null=False)

    group_id = models.PositiveIntegerField()
