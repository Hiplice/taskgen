# Generated by Django 3.2.4 on 2021-06-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0015_auto_20210624_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pattern',
            old_name='question',
            new_name='heading',
        ),
        migrations.AddField(
            model_name='pattern',
            name='question_body',
            field=models.TextField(null=True),
        ),
    ]
