import random, string, secrets
from tkinter import *
import tkinter as tk

root =Tk()
root.geometry("600x400") 
root.title("Andoni's Password Generator")
 
output_pass = StringVar()
 
all = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]  #list of all possible characters

#Password function
def randPassGen():
    password =""

    if var1.get() + var2.get() + var3.get() >1:
        while True:
            password = 'Please chose 1 option'
            break
    
    elif var1.get()== 1:
        while True:
            if pass_len.get() >0:
                password= ("".join([secrets.choice(string.digits) for i in range(pass_len.get())]))
                break
            else:
                continue
    
    elif var2.get()== 1:
        while True:
            if pass_len.get() >0:
                password= ("".join([secrets.choice(string.digits + string.ascii_letters) for i in range(pass_len.get())]))
                break
            else:
                continue

    elif var3.get()== 1:
        while True:
            if pass_len.get() >0:
                password= ("".join([secrets.choice(string.digits + string.ascii_letters + string.punctuation) for i in range(pass_len.get())]))
                break
            else:
                continue
    


    
    output_pass.set(password)
  
#GUI
 
pass_head = Label(root, text = 'Password Length', font = 'arial 12 bold').pack(pady=10)
 
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 24, font='arial 16').pack()
 
#Generate password button
 
Button(root, command = randPassGen, text = "Generate Password", font="Arial 12", fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

#Check Box 
var1 = tk.IntVar()
c1 = tk.Checkbutton(root, text='Numbers Only',variable=var1, onvalue=1, offvalue=0)
c1.pack()
var2 = tk.IntVar()
c1 = tk.Checkbutton(root, text='Numbers & Letters',variable=var2, onvalue=1, offvalue=0)
c1.pack()
var3 = tk.IntVar()
c1 = tk.Checkbutton(root, text='All Characters',variable=var3, onvalue=1, offvalue=0)
c1.pack()
 
pass_label = Label(root, text = 'Random Generated Password', font = 'arial 12 bold').pack(pady="30 10")
Entry(root , textvariable = output_pass, width = 24, font='arial 16').pack()
 
root.mainloop() 
