import time
start_time = time.time()
timing = int(input("How often do you want to be reminded?"))
while(True) :
    
    if ((time.time() - start_time) >= timing*60):
        print("Time is up! Take a break")
        start_time = time.time()
        timing = int(input("How often do you want to be reminded?"))






        


 

    