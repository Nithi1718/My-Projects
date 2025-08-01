#Calculator
print("Use this calculator to solve the following operation")
num1=int(input("Enter the first number: "))
print("Enter the operator = '+,-,*,/,//,%,**'")
operator=input("Enter the operator: ")
num2=int(input("Enter the second number: "))
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    if num2!=0:
        print(num1/num2)
    else:
        print("The number cannot be divided by 0")
elif operator=="//":
    if num2!=0:
        print(num1//num2)
    else:
        print("The number cannot be divided by 0")
elif operator=="%":
    if num2!=0:
        print(num1%num2)
    else:
        print("Error by 0")
elif operator=="**":
    print(num1**num2)
else:
    print()
    print('"Opeation error"')