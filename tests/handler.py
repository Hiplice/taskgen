from .models import Test, Topic
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
                               difficulty=generator.difficulty,
                               questions=json.dumps(questions),
                               answers=json.dumps(answers),
                               correct_answers=json.dumps(correct_answers))

    user.active_test = test.id
    user.save(update_fields=["active_test"])


def compare_result(request):
    n_questions = len(request.POST) - 1
    answers_accuracy = [0] * n_questions

    test_id = request.user.active_test
    db_test = Test.objects.get(id=test_id)
    correct_answers = json.loads(db_test.correct_answers)
    chosen_answers = [0]*n_questions

    for i in range(0, n_questions):
        chosen_answers[i] = int(request.POST["question_" + str(i + 1)])

    db_test.chosen_answers = json.dumps(chosen_answers)
    db_test.save()

    for i in range(n_questions):
        answers_accuracy[i] = correct_answers[i] == chosen_answers[i]

    return answers_accuracy
