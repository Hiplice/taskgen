from patterncomputer import compute_pattern
from .models import Question
from random import randint


def generate_answers(correct_answer, n_answers):
    answers = [0]*n_answers
    correct_position = randint(0, n_answers - 1)

    for i in range(n_answers):
        if i == correct_position:
            answers[i] = correct_answer
        else:
            answers[i] = randint(-50, 50)

    return answers


class TestGenerator:

    def __init__(self, topic_number, n_questions, n_answers):
        self.topic_number = topic_number
        self.n_questions = n_questions
        self.n_answers = n_answers
        self.questions = [0]*n_questions
        self.answers = [0]*n_questions
        self.correct_answers = [-1]*n_questions

        self.generate_questions()

    def generate_questions(self):
        all_patterns = Question.objects.filter(test_number=self.topic_number)
        total_patterns = len(all_patterns)
        used_patterns = set()

        for i in range(self.n_questions):
            generated_number = randint(0, total_patterns - 1)

            while generated_number in used_patterns:
                generated_number = randint(0, total_patterns - 1)

            self.questions[i], self.correct_answers[i] = compute_pattern(all_patterns[generated_number].text, '$')
            self.answers[i] = generate_answers(self.correct_answers[i], self.n_answers)

