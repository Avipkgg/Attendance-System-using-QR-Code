from tkinter.constants import GROOVE, RAISED, RIDGE
import cv2
import pyzbar.pyzbar as pyzbar
import time
from datetime import date, datetime
import tkinter as tk
from tkinter import Frame, ttk, messagebox
from tkinter import *

window = tk.Tk()
window.title('Faculty Attendance System For Library')
window.geometry('900x600')

Are_You_Ready_To_Start= tk.StringVar() 

Designation= tk.StringVar()
Branch= tk.StringVar()
Emp_ID= tk.StringVar()

title = tk.Label(window,text="Faculty Attendance System For Library",bd=10,relief=tk.GROOVE,font=("times new roman",40),bg="lavender",fg="black")
title.pack(side=tk.TOP,fill=tk.X)

Manage_Frame=Frame(window,bg="lavender")
Manage_Frame.place(x=0,y=80,width=480,height=530)

ttk.Label(window, text = "Are You Ready To Start :",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=150)
combo_search=ttk.Combobox(window,textvariable=Are_You_Ready_To_Start,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('Yes','No') 
combo_search.place(x=250,y=180)

def checkk():
    if(Are_You_Ready_To_Start.get()):
        window.destroy()
    else:
        messagebox.showwarning("Warning", "All fields required!!")

exit_button = tk.Button(window,width=13, text="Submit",font=("Times New Roman", 15),command=checkk,bd=2,relief=RIDGE)
exit_button.place(x=300,y=380)

Manag_Frame=Frame(window,bg="lavender")
Manag_Frame.place(x=480,y=80,width=450,height=530)

canvas = Canvas(Manag_Frame, width = 300, height = 300,background="lavender")      
canvas.pack()      
img = PhotoImage(file="Bg.png")      
canvas.create_image(50,50, anchor=NW, image=img) 

window.mainloop()

cap = cv2.VideoCapture(0)
names=[]
today=date.today()
d= today.strftime("%b-%d-%Y")

fob=open(d+'.xlsx','w+')
fob.write("Name"+'\t')
fob.write("Designation"+'\t')
fob.write("Emp_ID"+'\t')
fob.write("Branch"+'\n')
fob.write("In Time"+'\n')

def enterData(z):   
    if z in names:
        pass
    else:
        it=datetime.now()
        names.append(z)
        z=''.join(str(z))
        intime = it.strftime("%H:%M:%S")
        fob.write(z+'\t'+ Branch.get()+'-'+ Emp_ID.get()+'\t'+ Designation.get()+'\t'+intime+'\n')
    return names 

print('Reading...')

def checkData(data):
    #data=str(data)    
    if data in names:
        print('Already Present')
    else:
        print('\n'+str(len(names)+1)+'\n'+'present...')
        enterData(data)

while True:
    _, frame = cap.read()         
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        checkData(obj.data)
        time.sleep(1)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1)&0xFF == ord('g'):
        cv2.destroyAllWindows()
        break

fob.close()
