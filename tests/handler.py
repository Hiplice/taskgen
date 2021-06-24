from .models import *


class Question:
    def __init__(self, text, answers, correct_answer):
        self.text = text
        self.answers = answers
        self.correct_answer = correct_answer


def generate_question(topic, difficulty):
    available_patterns = Pattern.objects.filter(topic=topic)


def update_result(user, test, points):
    topic = test.topic
    test_object = TestData.objects.filter(user=user, topic=topic)

    if len(test_object) == 0:
        TestData.objects.create(user=user, topic=topic, attempts=1, best_result=points)
    else:
        test_object = test_object[0]
        test_object.attempts += 1
        test_object.best_result = points if points > test_object.best_result else test_object.best_result
        test_object.save(update_fields=['attempts', 'best_result'])


class Subject:

    def __init__(self, name, subject_id, topics):
        self.topics = topics
        self.subject_id = subject_id
        self.name = name


class TopicInformation:

    def __init__(self, name, topic_id, attempts, points):
        self.name = name
        self.topic_id = topic_id
        self.attempts = attempts
        self.points = points


def get_subject_information(request):
    user = request.user
    subjects = SubjectPermission.objects.filter(user=user)
    subject_info = []

    for permission in subjects:
        topics = Topic.objects.filter(subject=permission.subject)
        topic_info = []

        for topic in topics:
            test_data = TestData.objects.filter(user=user, topic=topic)

            if len(test_data) > 0:
                test_data = test_data[0]
                topic_info.append(TopicInformation(topic.name, topic.id, test_data.attempts, test_data.best_result))
            else:
                topic_info.append(TopicInformation(topic.name, topic.id, 0, 0))
        subject_info.append(Subject(permission.subject.name, permission.subject.id, topic_info))

    return subject_info



