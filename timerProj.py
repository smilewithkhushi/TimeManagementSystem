import time


# Python program to get
# current date
# Import date class from datetime module
from datetime import date
# Returns the current local date
today = date.today()
print("\nToday date is: ", today)

print()
countdownVal=int(input("Set your countdown timer (in sec) here : "))
print()
def countdown(time_sec):
    while time_sec:
        mins=time_sec//60
        secs=time_sec%60
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("\n STOP \n")

countdown(countdownVal)


print("What shall I remind you about ?? ", end="")
text = str(input())
local_time = int(input("In how many minutes? "))
local_time = local_time * 60
countdown(local_time)
time.sleep(local_time)
print(text)


# importing whole module
from tkinter import *
from time import strftime
root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title('Python Clock')
Label(root,text = 'TIMER', font ='arial 20 bold').pack(side=BOTTOM)
def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)
mark = Label(root, 
            font = ('calibri', 40, 'bold'),
            pady=150,
            foreground = 'black')
mark.pack(anchor = 'center')
time()
 
mainloop()
