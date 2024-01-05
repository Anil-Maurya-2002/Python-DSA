# 34 Scope,Global Varibles & Keyword

l =10    # Global varibel
def function1(n):
    l = 5   # Local vasibles
    m = 8   # Local vasibles
    print(l, m)
    #print(n, "i have printed")

print(l)


x=80
def anil():
    x=30
    def rahul():
        global  x    # this global is final global
        x= 50
    rahul()
    print("after calling rahul()", x)
anil()
print(x)