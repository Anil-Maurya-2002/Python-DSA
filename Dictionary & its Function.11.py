# 11 Dictionary & its Function
# Dictionary is Key value paires - Immutable = { }
d1 =()
d2 ={}
d3 =[]
print(type(d1))
print(type(d2))
print(type(d3))

d1 =(1,2)
d2 ={3,4}
d3 =[5,6]
print(type(d1))
print(type(d2))
print(type(d3))
print(d3)

""" 
d1 =(a,bb)
d2 ={cc,ddd }
d3 =[ee,fff]
print(type(d1))
print(type(d2))
print(type(d3))
"""
d1={"anil":"studant","23":"rahul","25":"50"}
print(d1["anil"],["23"])
print(d1.keys())
print(d1.items())
d2=d1.copy()
print(d2)