# 35 Recursion & Iteritive
# Recursion mean function k ander function use krna
# n!= n*n-1 *n-2 * n-3 .....1
# n! = n* (n-1)!
""""

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
    pass
numbers = int(input("Enter then number\n"))
print("Factorial using iterative method\n ",factorial_iterative(numbers))

""

# use recursive
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n* factorial_recursive(n-1)
    # 5* factorial_recursive(4)
    # 5*4* factorial_recursive(3)
    # 5*4*3* factorial_recursive(2)
    # ...
    # 5*4*3*2*1 =120
numbers=int(input("Enter then number\n"))
print("Factorial using recursive method\n",factorial_recursive(numbers))

"""

# Fibonacci series
# 0 1 1 2 3 5 8 13....
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
numbers=int(input("Enter the position of number\n"))
print("Value of number\n",fibonacci(numbers))
