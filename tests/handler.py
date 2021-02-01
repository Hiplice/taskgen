from .models import *
import json


def create_test(generator, request):
    n_tests = generator.n_questions
    questions = [0] * n_tests
    answers = [0] * n_tests
    correct_answers = [0] * n_tests

    for i in range(n_tests):
        questions[i] = generator.questions[i].text
        answers[i] = generator.questions[i].answers
        correct_answers[i] = generator.questions[i].correct_answer

    topic = Topic.objects.get(id=generator.topic_number)

    user = request.user
    test = Test.objects.create(user=user,
                               topic=topic,
                               questions=json.dumps(questions),
                               answers=json.dumps(answers),
                               correct_answers=json.dumps(correct_answers))

    user.active_test = test.id
    user.save(update_fields=["active_test"])


def compare_result(request):
    n_questions = len(request.POST) - 1
    n_correct_answers = 0

    test_id = request.user.active_test
    db_test = Test.objects.get(id=test_id)
    correct_answers = json.loads(db_test.correct_answers)
    chosen_answers = [0]*n_questions

    for i in range(0, n_questions):
        chosen_answers[i] = int(request.POST["question_" + str(i + 1)])

    db_test.chosen_answers = json.dumps(chosen_answers)
    db_test.save(update_fields=["chosen_answers"])

    user = request.user
    user.active_test = None
    user.save(update_fields=["active_test"])

    for i in range(n_questions):
        n_correct_answers += 1 if correct_answers[i] == chosen_answers[i] else 0

    update_result(user, db_test, n_correct_answers)

    return n_correct_answers


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


class TopicInformation:

    def __init__(self, name, topic_id, attempts, points):
        self.name = name
        self.topic_id = topic_id
        self.attempts = attempts
        self.points = points


def get_topic_information(request):
    topics = Topic.objects.all()
    user = request.user
    topic_info = []

    for topic in topics:
        test_data = TestData.objects.filter(user=user, topic=topic)

        if len(test_data) > 0:
            test_data = test_data[0]
            topic_info.append(TopicInformation(topic.name, topic.id, test_data.attempts, test_data.best_result))
        else:
            topic_info.append(TopicInformation(topic.name, topic.id, 0, 0))

    return topic_info


def add_test(request):
    Pattern.objects.create(
        topic=Topic.objects.get(id=request.POST['topic']),
        question=request.POST['question'],
        expression=request.POST['expression'],
        generate_from=request.POST['generate_from'],
        generate_to=request.POST['generate_to'],
        answer_from=request.POST['answer_from'],
        answer_to=request.POST['answer_to']
    )





