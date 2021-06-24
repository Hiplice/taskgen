from random import randint


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
            answers[i] = randint(answers_from, answers_to)

    return answers