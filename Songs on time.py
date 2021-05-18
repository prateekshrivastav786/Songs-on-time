
# coding: utf-8

# In[45]:
# Prateek

import datetime # to get the time of the system
import webbrowser # to open the web url
import time
t=str(datetime.datetime.now()) # taking the current time in a variable as a string

if t[11:19]== "07:22:25":           # user's selected time
    print("Your song is playing!!!")
    webbrowser.open('https://www.youtube.com/watch?v=jCXN3BKA9dE')   # opening the website of song
  
elif t[11:19] > "07:22:25" and t[11:19] < "08:22:22":
    print("Your song is waiting for you!!! Playing...")
    webbrowser.open('https://www.youtube.com/watch?v=vCoi_p7drek')
    
elif t[11:19] == "09:00:00":
    print("news time")
    time.sleep(1)
    webbrowser.open('https://www.irishtimes.com/')
    
else:
    print("Sorry!!!")
    print("No song lined up for you now, Please go for your study")
    time.sleep(4) # halting the program for 4 seconds
    print("\tJust Kidding!!! I know you won't")
    time.sleep(2)
    print("You have this great song...")
    time.sleep(2)
    webbrowser.open('https://www.youtube.com/watch?v=pldIIwmdqlQ')
print("\nThe current time is:", t)


# In[ ]:



