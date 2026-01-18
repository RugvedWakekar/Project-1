def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operation_dictionary = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}

def calculator():
    should_continue = True
    num1 = float(input('Enter the first number: \n'))
    while should_continue:
        for key in operation_dictionary:
            print(key)

        operation = input('Pick an operation: ')
        num2 = float(input('Enter the second number: \n'))
        result = operation_dictionary[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {result}")
        again = input(f"Type 'y' to continue calculating with {result}, else type 'n' to start a new calculation: ").lower()

        if again == 'y':
            num1 =  result

        elif again == 'n':
            should_continue = False
            print(f'Your final result is {result}, Thank you')
        else:
            print('Invalid input, enter y or n only')

calculator()


