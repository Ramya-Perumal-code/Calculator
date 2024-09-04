from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return  n1 / n2

calc_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    """ Function to perform arithmatic operation"""
    print(logo)
    loop = True
    a = float(input("What's the first number?: "))
    temp_result = a
    while loop:
        for key in calc_dict:
            print(key)
        opr = input("Pick an operation: ")
        b = float(input("What's the next number?: "))
        result = calc_dict[opr](temp_result,b)
        print(f"{temp_result} {opr} {b} = {result}")
        temp_result = result
        should_continue = input(f"Type 'y' to continue calculating with {temp_result}, or type 'n' to start a new calculation:  ").lower()
        if should_continue == 'n':
            loop = False
            calculator()

calculator()

