def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2
def calculator():
    from art import logo
    print(logo)
    operation={
        "+":add,
        "-":subtract,
        "*":multiply,
        "/":divide}
    continuation=True
    output=0
    number1=float(input("enter the first number "))
    while continuation:
        print(f"{number1}")
        operator = input("what is the operator you want to use ")
        number2=float(input("enter the second number "))
        output=operation[operator](number1,number2)
        print(f"{number1}{operator}{number2}={output}")
        continuation_question=input("(y) for continue (n) for new calculation (c) for end program ")
        if continuation_question=="y":
            number1=output
        elif continuation_question=="n":
            continuation=False
            print("\n"*100)
            calculator()
        elif continuation_question=="c":
            print("thank you, have a nice day")
            break
        else:
            print("invalid input")


calculator()