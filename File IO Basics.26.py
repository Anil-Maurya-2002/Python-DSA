# 26  File IO Basics
"""
"r" - Open file for reading
"w" - Open file for writing
"x" - Creates file if not exists
"a" - Add more content to a file (a = appending)
"t" - Text mode  ( default )
"b" - Binary mode
"+" - Read and Write

"""

# 27 0pen(),read(),...
f = open("Anil")
content =f.read()
print(content)
f.close()