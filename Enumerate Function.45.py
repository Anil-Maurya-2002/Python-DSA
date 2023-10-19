# 45 Enumerate Faction
a = [ "apple","mango","banana","orange"]
i=1
for item in a:
    if i%2 != 0:
        print( {item} )
        i += 1

#
for index, item in enumerate(a):
    if index%2 == 0:
        print({item})
