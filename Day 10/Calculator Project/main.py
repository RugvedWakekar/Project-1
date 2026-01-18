def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operation_dict ={
    '+':add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
# import art
# print(art.logo)
# print("+\n-\n*\n/")
def calculator():
    should_continue = True
    import art
    print(art.logo)
    num1 = float(input('Enter your first number: \n'))
    while should_continue:
        for symbol in operation_dict:
            print(symbol)

        operation = str(input('Pick an operation: '))
        num2 = float(input('Enter your second number: \n'))
        result = operation_dict[operation](num1,num2)

        print(f"{num1} {operation} {num2} = {result}")
        again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if again == 'y':
            num1 = result
        elif again == 'n':
            should_continue = False
            print("\n"*20)
            calculator()
        else:
            print("Invalid input, type 'y' or 'n' only")

calculator()