import tkinter as tk
import ast
import operator
import re

#Dictionary
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
    '%': operator.mod
}

#operation function
def evaluate_expression(expression):
    expression = re.sub(r'\s+', '', expression)
    tokens = re.findall(r'\d+|\*\*|\+|\-|\*|\/|%', expression)

    if not tokens:
        return "Invalid!"

    numbers = []
    operations = []

    for token in tokens:
        if token.isdigit():
            numbers.append(ast.literal_eval(token))
        elif token in ops:
            operations.append(token)
        else:
            return "Invalid!"

    result = numbers[0]
    for i in range(len(operations)):
        result = ops[operations[i]](result, numbers[i + 1])

    return result


def button_click(symbol):
    current_text = entry_var.get()
    entry_var.set(current_text + symbol)

def calculate():
    try:
        result = evaluate_expression(entry_var.get())
        entry_var.set(result)
    except Exception:
        entry_var.set("Error")

def clear():
    entry_var.set("")


root = tk.Tk()
root.title("Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root,
                 textvariable=entry_var,
                 font=("Arial", 18),
                 justify="right")
entry.grid(row=0,
           column=0,
           columnspan=4,
           ipadx=8,
           ipady=8)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    action = lambda x=text: button_click(x) if x != "=" else calculate()
    tk.Button(root,
              text=text,
              font=("Arial", 14),
              command=action,
              width=5,
              height=2).grid(row=row, column=col)

tk.Button(root,
          text="C",
          font=("Arial", 14),
          command=clear,
          width=5,
          height=2,
          fg="red").grid(row=5, column=0, columnspan=4, sticky="we")

root.mainloop()
