def calculator(num1, num2, operator):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="/":
        return num1/num2

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
operator = input("Enter operator as string: ")
print(calculator(num1, num2, operator))