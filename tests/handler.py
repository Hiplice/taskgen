from .models import *
from . import generate
from json import dumps, loads
global_pattern = Pattern.objects.get(id=6)


def check_answer(user, answer):
    test = Test.objects.get(id=user.active_test)
    point = 0
    global global_pattern
    # Добавляем очки за правильный ответ
    if answer == str(test.last_question.correct_answer):
        if test.last_question.difficulty == 3:
            test.points += 3
        elif test.last_question.difficulty == 2:
            test.points += 2
        else:
            test.points += 1
        test.streak += 1
    else:
        if test.last_question.difficulty == 3:
            test.streak = 3
            test.save()
            return False
        else:
            test.streak = 0
    test.save()
    db_questions_data = QuestionsData(
        difficulty=test.last_question.difficulty,
        correct_answer=test.last_question.correct_answer,
        user_answer=answer,
        heading=test.last_question.heading,
        body=test.last_question.body,
        answers=dumps(test.last_question.answers),
        pattern=global_pattern,
        test=test,
        counter=test.question_count,
        point=point
    )
    db_questions_data.max_point=db_questions_data.difficulty+1
    db_questions_data.save()
    point = 0
    return test.streak > 0


def create_question(test):
    if test.streak > 5 and len(Pattern.objects.filter(topic=test.topic_id, difficult=3)) > 0:
        difficult = 3
    elif test.streak > 2 and len(Pattern.objects.filter(topic=test.topic_id, difficult=2)) > 0:
        difficult = 2
    else:
        difficult = 1
    pattern, question = generate.generate_question(topic=test.topic_id, difficulty=difficult)
    global global_pattern
    global_pattern = pattern
    # Создаю новый Question
    db_question = Question(
        difficulty=pattern.difficult,
        correct_answer=question.correct_answer,
        heading=question.heading,
        body=question.body,
        answers=dumps(question.answers)
    )
    db_question.save()
    test.last_question.delete()
    test.last_question = db_question
    test.question_count += 1
    test.save()


def get_test_data(test_id):
    test = Test.objects.get(id=test_id)
    questions = test.last_question
    questions.answers = loads(questions.answers)
    return test, questions


def create_test(user, topic):
    pattern, question = generate.generate_question(topic, 1)
    global global_pattern
    global_pattern = pattern
    # Создаём объект вопроса в бд
    db_question = Question(
        difficulty=pattern.difficult,
        correct_answer=question.correct_answer,
        heading=question.heading,
        body=question.body,
        answers=dumps(question.answers)
    )
    db_question.save()

    # Создаём объект теста в бд
    db_question.answers = loads(db_question.answers)
    test = Test(user=user, topic_id=topic, last_question_id=db_question.id)
    test.save()
    user.active_test = test.id
    user.save()

    return db_question, test


def update_result(user):
    test = Test.objects.get(id=user.active_test)
    test.last_question.delete()
    topic = test.topic
    test_object = TestData.objects.filter(user=user, topic=topic)
    user.active_test = None
    user.save()

    if len(test_object) == 0:
        TestData.objects.create(user=user, topic=topic, attempts=1, best_result=test.points)
    else:
        test_object = test_object[0]
        test_object.attempts += 1
        test_object.best_result = test.points if test.points > test_object.best_result else test_object.best_result
        test_object.save(update_fields=['attempts', 'best_result'])


class SubjectInfo:
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
    subjects = Subject.objects.filter(topic__exact=True)
    subject_info = []

    for subject in subjects:
        topics = Topic.objects.filter(subject=subject)
        topic_info = []

        for topic in topics:
            if len(Pattern.objects.filter(topic=topic, difficult=1)) > 0 or len(Pattern.objects.filter(topic=topic, difficult=2)) > 0 or len(Pattern.objects.filter(topic=topic, difficult=3)) > 0:
                test_data = TestData.objects.filter(user=user, topic=topic)

                if len(test_data) > 0:
                    test_data = test_data[0]
                    topic_info.append(TopicInformation(topic.name, topic.id, test_data.attempts, test_data.best_result))
                else:
                    topic_info.append(TopicInformation(topic.name, topic.id, 0, 0))
        subject_info.append(SubjectInfo(subject.name, subject.id, topic_info))

    return subject_info
