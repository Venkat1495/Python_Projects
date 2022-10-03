# Calculator

def add(n1, n2):
    """Performing addition between n1 and n2"""
    return n1 + n2

def sub(n1, n2):
    """Performing subtract between n1 and n2"""
    return  n1 - n2

def multiply(n1, n2):
    """Performing multiply between n1 and n2"""
    return n1 * n2

def divide(n1, n2):
    """Performing divide between n1 and n2"""
    return n1 / n2

cal_dis = {
    '+': add,
    '-': sub,
    '*': multiply,
    '/': divide
}
def calculator():
    """Doing '+, -, *, /,' between two numbers"""
    num1 = float(input("What's the first number?: "))
    for symbol in cal_dis:
        print(symbol)
    is_while = True
    while is_while:
        op_symbol = input("Pick an operation from above: ")
        num2 = float(input("What's the next number?: "))
        function = cal_dis[op_symbol]
        result = function(num1, num2)
        print(f"{num1} {op_symbol} {num2} = {result}")
        type = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculator, or type 'e' to exit: ")
        if type == 'y':
            is_while = True
            num1 = result
        elif type == 'n':
            calculator()
        else:
            is_while = False

calculator()
