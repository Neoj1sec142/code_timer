from tkinter import *
from tkinter import messagebox as mb
import time
import sys
win = Tk()
win.geometry('750x300')
win.resizable(1,1)
win.title('Py Timer')
win.config(bg='gray')
sec = StringVar()
Entry(win, textvariable=sec, width = 2, font = 'Serif 14').place(x=220, y=120)
sec.set('00')
mins= StringVar()
Entry(win, textvariable = mins, width =2, font = 'Serif').place(x=180, y=120)
mins.set('00')
hrs= StringVar()
Entry(win, textvariable = hrs, width =2, font = 'Serif 14').place(x=142, y=120)
hrs.set('00')
times = 0
def thetimer():
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
      minute,second = (times // 60 , times % 60)
      hour =0
      if minute > 60:
         hour , minute = (minute // 60 , minute % 60)
      sec.set(second)
      mins.set(minute)
      hrs.set(hour)
      #Update the time
      win.update()
      time.sleep(1)
      if(times == 0):
         sec.set('00')
         mins.set('00')
         hrs.set('00')
      times += 1

label = Label(win, font=("Courier", 30, 'bold'), bg="blue", fg="white", bd =30)
label.grid(row =0, column=1)
label.place(x=300, y=100)
def digitalclock():
   text_input = time.strftime("%H:%M:%S")
   label.config(text=text_input)
   label.after(200, digitalclock)
digitalclock()

def exit():
    inp = mb.askyesno("QUIT?", "Are you sure you wish to quit?")
    if inp == True:
        sys.exit()


Label(win, font =('Serif bold',22), text = 'Start the Timer',bg='white').place(x=105,y=70)
Button(win, text='START', bd ='2', bg = 'IndianRed1',font =('Serif',10), command = thetimer).place(x=167, y=165)
Button(win, text='Exit', bd ='2', bg = 'IndianRed1',font =('Serif',10), command = exit).place(x=100, y=165)
win.mainloop()