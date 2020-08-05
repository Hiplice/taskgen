from random import randint


def replace_sign(pattern, pattern_sign):
    n_patterns = pattern.count(pattern_sign)

    for i in range(n_patterns):
        symbol_index = pattern.find(pattern_sign)
        generated_number = str(randint(1, 10))
        pattern = pattern[:symbol_index] + generated_number + pattern[symbol_index + len(pattern_sign):]

    return pattern


def execute_code(pattern):
    def set_execution_result(res):
        global result
        result = res

    pattern = pattern.replace("print", "set_execution_result")
    exec(pattern)

    return result