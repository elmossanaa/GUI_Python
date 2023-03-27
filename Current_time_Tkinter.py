from tkinter import *

from time import strftime

t = Tk()
t.title("Current Time")

def digital_current_time():
    time = strftime('%H:%M:%S %p ')
    #strftime: used to give user the current time
    digit_time.config(text = time)
    digit_time.after(200,digital_current_time )
    #200 represents the millisend time

digit_time  = Label(t, font = ("Verdana", 60), bg ="#8FBC8F", fg = "LightCoral")
digit_time.pack()

digital_current_time()
                    

mainloop()
