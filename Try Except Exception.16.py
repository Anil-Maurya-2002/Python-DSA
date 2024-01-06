# 25 Try Except Exception Handling ( simple )
print("enter num 1")
num1=input()
print("enter num2")
num2=input()
print("sum of two no is",
      int(num1)+int(num2))
print("This line is important\n")


# 25 Try Except Exception Handling
print("enter num 1")
num1=input()
print("enter num2")
num2=input()
try:
    print("sum of two no is",
      int(num1)+int(num2))
except Exception as a:  # All code are run except only wrong, if i/p not use int valu (valide)
    print(a)
print("This line is important")