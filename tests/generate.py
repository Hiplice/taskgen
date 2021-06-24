from random import randint
from .models import Pattern


def replace_sign(pattern, pattern_sign, generate_from, generate_to):
    n_patterns = pattern.count(pattern_sign)

    for i in range(n_patterns):
        symbol_index = pattern.find(pattern_sign)
        generated_number = str(randint(generate_from, generate_to))
        pattern = pattern[:symbol_index] + generated_number + pattern[symbol_index + len(pattern_sign):]

    return pattern


def execute_code(pattern):
    def set_execution_result(res):
        global result
        result = res

    pattern = pattern.replace("print", "set_execution_result")
    exec(pattern)

    return result


def compute_pattern(pattern, pattern_sign, generate_from, generate_to):
    '''
    :param pattern: Gets a pattern for execution
    :param pattern_sign: Gets a sign for pattern
    :return: Returns code with numbers without parameters and pattern execution result
    '''

    final_code = replace_sign(pattern, pattern_sign, generate_from, generate_to)
    execution_result = execute_code(final_code)

    return final_code, execution_result


def generate_answers(correct_answer, n_answers, answers_from, answers_to):
    answers = [0]*n_answers
    correct_position = randint(0, n_answers - 1)

    for i in range(n_answers):
        if i == correct_position:
            answers[i] = correct_answer
        else:
            current_answer = randint(answers_from, answers_to)
            while current_answer in answers:
                current_answer = randint(answers_from, answers_to)
            answers[i] = current_answer

    return answers


class Question:
    def __init__(self, heading, body, answers, correct_answer):
        self.heading = heading
        self.body = body
        self.answers = answers
        self.correct_answer = correct_answer


def generate_question(topic, difficulty):
    available_patterns = Pattern.objects.filter(topic=topic, topic__pattern__difficult=difficulty)
    chosen_pattern = available_patterns[randint(0, len(available_patterns) - 1)]
    text, correct_ans = compute_pattern(chosen_pattern.expression, "$", chosen_pattern.generate_from, chosen_pattern.generate_to)

    return chosen_pattern, Question(
        heading=chosen_pattern.heading,
        body=text,
        correct_answer=correct_ans,
        answers=generate_answers(correct_ans, 4, chosen_pattern.answer_from, chosen_pattern.answer_to)
    )