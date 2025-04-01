import ast
import operator
import re

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
    '%': operator.mod
}

def evaluate_expression(expression):
    expression = re.sub(r'\s+', '', expression)
    tokens = re.findall(r'\d+|\*\*|\+|\-|\*|\/|%', expression)

    if not tokens:
        return "Invalid Expression!"

    numbers = []
    operations = []

    for token in tokens:
        if token.isdigit():
            numbers.append(ast.literal_eval(token))
        elif token in ops:
            operations.append(token)
        else:
            return "Invalid Expression!"

    result = numbers[0]
    for i in range(len(operations)):
        result = ops[operations[i]](result, numbers[i + 1])

    return result

while True:
    try:
        expression = input("Masukkan nilai (ketik 'exit' jika ingin keluar): ")

        if expression.lower() == 'exit':
            break

        result = evaluate_expression(expression)
        print(f"Hasil: {result}")

    except Exception as e:
        print(f"Error: {e}. Pastikan input valid!")
