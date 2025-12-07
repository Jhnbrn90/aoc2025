import re 

from math import prod


def calculate_right_left_problem(problem_input: list[str]) -> int:
    symbol = problem_input.pop()
    
    list_of_integers = [''.join(col) for col in zip(*problem_input)]
    list_of_integers = [re.sub(' ', '', i) for i in list_of_integers if i.strip()]
    list_of_integers = [int(i) for i in list_of_integers]

    math_operation = {
        '+': lambda x: sum(x),
        '*': lambda x: prod(x),
    }

    return math_operation[symbol](list_of_integers)


def parse_input_string_to_grid(math_problems_input: str) -> list[list[str]]:
    """Convert single string input to matrix of math problem strings."""
    rows = math_problems_input.split('\n')

    matrix = []

    for row in rows:
        row_tokens = []
        tokens = row.split(' ')
        padding = max([len(token) for token in tokens])

        for i, token in enumerate(tokens):
            if len(token) < padding:
                number_of_tokens_short = padding - len(token)
                if i > 0 and tokens[i-1] == '' and token != '':  # padd left
                    token_string = number_of_tokens_short * ' ' + token
                    row_tokens.append(token_string)
                elif i < len(tokens)-1 and tokens[i+1] == '' and token != '':  # padd left
                    token_string = token + number_of_tokens_short * ' '
                    row_tokens.append(token_string)
            else:
                row_tokens.append(token)

        if not row_tokens == ['']:
            matrix.append([token for token in row_tokens])
        
    return matrix
