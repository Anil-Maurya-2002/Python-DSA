"""
# 15 Exercise 1
d = {'anil':'20.08.2002',
     'deepak':'25.10.2003',
     'pawan':'1.1.2003'}
name =input("Enter the name\n ")
print(d[name])
"""
# 16 Exercise 2  (#20 solution)
# faulty calculater
# 45*3=555, 56+9=77, 56/6=4
num1=int(input("Enter 1st no\n"))
num2=int(input("Enter 2nd no\n"))
operater=input("Enter operater you need to proferm *,+,/ ,-,\n")
if num1==45 and num2==3 and operater=='*':
     print(555)
elif num1==56 and num2==9 and operater=='+':
     print(77)
elif num1==56 and num2==6 and operater=='/':
     print(4)
elif operater=='*':
     print(num1*num2)
elif operater=='+':
     print(num1+num2)
elif operater=='/':
     print(num1/num2)
elif operater=='-':
     print(num1-num2)

