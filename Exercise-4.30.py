# 30 Pattern Printing
# Exercise

print("Pattern printing")
num=int(input("Enter num how many row want to print\n"))
for i in range (0,num+1):
    print("*"*i)


num=int(input("Enter num how many row want to print\n"))
for i in range (num,0,-1):
    print("*"*i)

""""
# for 1 - *
# for 0 - #
num= int(input("Enter the no. how many row print\n"))
print("Enter 1 or 0")
bool_val = int(input("1 for True value or 0 for False\n"))
if bool_val == "1":
    for i in range (0,num+1):
        print("*"*i)
if bool_val == "0":
    for i in range(num,0,-1):
        print("*"*i)


"""