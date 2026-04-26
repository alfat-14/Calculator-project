def add(a, b):
    return a + b



def sub(a, b):
    return a - b



def mul(a, b):
    return a * b



def div(a, b):
    if b == 0:
        return "You Can't divide by zero"
    return a / b




def rem(a, b):
    if b == 0:
        return "You can't modulo by zero"
    return a % b




while True:
    a = input("Enter first number (enter exit to exit): ")
    if a == "exit":
        print("Goodbye")
        break
    try:
        a = int(a)
        b = int(input("Enter second number: "))
    except:
        print("Invalid input")
        continue

    c = input("Enter your operator (+, -, *, /, %): ")


    if c == "+":
        result = add(a, b)
    elif c == "-":
        result = sub(a, b)

    elif c == "*":
        result = mul(a, b)
    elif c == "/":
        result = div(a, b)

    elif c == "%":
        result = rem(a, b)
    else:
        print("Invalid operator")
        continue

    print("Result: ", result)












