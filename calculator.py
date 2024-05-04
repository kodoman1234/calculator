def calculator(x,y,ops):
    if ops not in "+-*/":
        return "Only +-*/ !!!"
    if ops == "+":
        return (str(x) + " " + ops + " " + str(y) + " = " + str(x+y))
    elif ops == "-":
        return (str(x) + " " + ops + " " + str(y) + " = " + str(x-y))
    elif ops == "*":
        return (str(x) + " " + ops + " " + str(y) + " = " + str(x*y))
    elif ops == "/":
        return (str(x) + " " + ops + " " + str(y) + " = " + str(x/y))
while True:
    x = int(input("Please type the first number: "))
    y = int(input("Please type the second number: "))
    ops = input("Choose between +, -, *, /: ")
    print(calculator(x,y,ops))

