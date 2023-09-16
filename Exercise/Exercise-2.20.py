# 20 Exercise 2 Falty calculator
num1=int(input("enter the first number\n"))
num2=int(input("Enter the second number\n"))
operator=input("Enter the operator you need to perform /,*,-,+\n")

if num1==45 and num2==3 and operator=='*':
    print(555)
elif num1==56 and num2==9 and operator=='+':
    print(77)
elif num1==56 and num2==9 and operator=='/':
    print(4)
elif operator=='+':
    print(num1+num2)
elif operator=='*':
    print(num1*num2)
elif operator=='/':
    print(num1/num2)
else:
    print("you have done wrong calcualtion")
