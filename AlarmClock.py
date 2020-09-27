#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import *
import time
import os

#Basic Clock GUI
win = Tk()
win.configure(background = "LightGrey")
win.title("Alarm Clock")

example = Label(win, font = ('times', 80, 'bold'), background = 'Black', foreground = 'White')
example.pack(fill = BOTH, expand = 1)

e1 = Entry(win)
e1.pack()

def setal():
    t = e1.get()
    if (t == time.strftime('%H:%M:%S')):
        os.system('BadDay-KuLam_p4k2.mp3') #Play mp3 file as alarm

#Button to Set Alarm time
bt = Button(win, text = 'Set Alarm', background = 'LightGrey', command = setal).pack()

#Time change in clock
def passtime():
    a = time.strftime('%H:%M:%S')
    if (a != example["text"]):
        example["text"] = a
    setal()
    example.after(200, passtime)

passtime()
win.mainloop()
#Nhập đúng theo định dạng giờ ở "Set Alarm"


# In[ ]:




