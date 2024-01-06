# 43 Time Module
# Time modul- tell about the program how much time is required
# Slip modul- tell about the progeam how much time is sleep/wait for excuting/output

import time

# Time modul

initial = time.time()
k=0
while (k<10):
    print("This is time modul")

    time.sleep( 2 )   # Sleep modul - tell how much time sleep/wait

    k+=1
print("Whil loop ran in",time.time()- initial,"Seconds")
initial2 =time.time()
for i in range(10):
    print("this is time modul")
print("Whil loop ran",time.time()- initial2,"Seconds")

"""

localtime = time.asctime(time.localtime(time.time()))  # tell about real time
print(localtime)

"""