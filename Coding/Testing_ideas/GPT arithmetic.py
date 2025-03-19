def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        first_line.append(operand1.rjust(width))
        second_line.append(operator + ' ' + operand2.rjust(width - 2))
        dash_line.append('-' * width)

        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answer_line.append(answer.rjust(width))

    arranged_problems = '    '.join(first_line) + '\n'
    arranged_problems += '    '.join(second_line) + '\n'
    arranged_problems += '    '.join(dash_line)

    if show_answers:
        arranged_problems += '\n' + '    '.join(answer_line)

    return arranged_problems

print(arithmetic_arranger(["100 - 32", "13 + 4", "1000 + 1"]))