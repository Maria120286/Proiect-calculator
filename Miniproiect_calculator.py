"""
Se ruleaza scriptul
Se incepe operatiunea cu o adunare sau o inmultire: ex "+5" iar calculatorul va avea in memorie acel 5
Pe urma se pot face operatii de adunare, scadere, inmultire si impartire
ex: 
+5 -> in memorie 5
-3 -> o sa calculeze 5-2 = 3 iar in memorie o sa ramana 3
*3 -> o sa calculeze 3*3
si asa mai departe

"""


import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Invalid operation")
        return x
    else:
        return x / y

def set_value(x, y):
    return y

def exit_program(x, y):
    print("Ieșire din program.")
    sys.exit()

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '=': set_value,
    'x': exit_program
}

# Set the initial value from command line arguments, or 0 if not provided
initial_value = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0

while True:
    print(initial_value)
    operation = input("> ")

    if len(operation) < 2 or operation[0] not in operations or not operation[1:].lstrip('-').replace('.', '', 1).isdigit():
        print("Invalid operation")
        continue

    operator = operation[0]
    number = float(operation[1:])

    initial_value = operations[operator](initial_value, number)
