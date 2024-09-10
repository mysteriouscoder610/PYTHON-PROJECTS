from time import *
import random as r

def mistake(para, usertest):
      error = 0;
      for i in range(len(para)):
            try:
                 if para[i]!=usertest[i]:
                       error = error+1
            except:
                 error = error+1
      return error 

def speed_time(time_s, time_e, userinput):
      timedelay = time_e - time_s
      time_roundoff = round(timedelay, 2)
      speed = len(userinput)/time_roundoff
      return round(speed)

test=["this is a very beautifull paragraph",
      "My name is Ayush Jha","Welcome to My world"]

test1 = r.choice(test)
print("******* TYPING SPEED *******")
print(test1)
print()
print()

time1 = time()
testinput = input("Enter : ")
time2 = time()

print('Speed : ',speed_time(time1, time2, testinput), " word per second")
print("Error : ", mistake(test1, testinput))
input("Press Enter to exit...")
