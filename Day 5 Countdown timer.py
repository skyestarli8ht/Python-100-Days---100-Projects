import time
# ***** Countdown Timer *****

#Step 1: Get user input in Seconds
duration = int(input("Enter the Countdwon Duration (in Seconds): "))

#step 2: Start countdown
print("##### Countdown Begin #####")
while duration > 0:
    print(f"{duration}s")
    time.sleep(1)
    duration -= 1

#Step 3: Final message
print("Time is Up!!!")  


#updation 
#ask user for speed of countdown