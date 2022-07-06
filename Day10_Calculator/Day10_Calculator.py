from art import logo
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def devide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : devide
}
def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("What's the first number? : "))
    for symbol in operations:
        print(symbol)
    while should_continue:
        operation_symbol = input("Pick an operation : ")
        next_num = float(input("What's the next number? : "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, next_num)
        print(f"{num1} {operation_symbol} {next_num} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculations : ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()