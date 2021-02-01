from patterncomputer import compute_pattern
from random import randint
from .models import Pattern, Topic


def generate_answers(correct_answer, n_answers, answers_from, answers_to):
    answers = [0]*n_answers
    correct_position = randint(0, n_answers - 1)

    for i in range(n_answers):
        if i == correct_position:
            answers[i] = correct_answer
        else:
            answers[i] = randint(answers_from, answers_to)

    return answers


class OneQuestion:

    def __init__(self, text, answers, correct_answer, number):
        self.text = text
        self.answers = answers
        self.correct_answer = correct_answer
        self.number = number


class TestGenerator:

    def __init__(self, topic_number, n_questions, n_answers):
        self.topic_number = topic_number
        self.n_questions = n_questions
        self.n_answers = n_answers
        self.questions = [0] * n_questions

        self.generate_questions()

    def generate_questions(self):
        all_patterns = Pattern.objects.filter(topic=self.topic_number)
        total_patterns = len(all_patterns)
        used_patterns = set()

        for i in range(self.n_questions):
            generated_number = randint(0, total_patterns - 1)

            while generated_number in used_patterns:
                generated_number = randint(0, total_patterns - 1)

            question, correct_answer = compute_pattern(all_patterns[generated_number].expression, '$', all_patterns[generated_number].generate_from, all_patterns[generated_number].generate_to)
            answers = generate_answers(correct_answer, self.n_answers, all_patterns[generated_number].answer_from, all_patterns[generated_number].answer_to)

            self.questions[i] = OneQuestion(question, answers, correct_answer, i + 1)