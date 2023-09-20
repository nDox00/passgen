import random, string
from tkinter import *

root =Tk()
root.geometry("600x400") 
root.title("Andoni's Password Generator")
 
output_pass = StringVar()
 
all = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]  #list of all possible characters

#Password function
def randPassGen():
    password =""
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
 
pass_label = Label(root, text = 'Random Generated Password', font = 'arial 12 bold').pack(pady="30 10")
Entry(root , textvariable = output_pass, width = 24, font='arial 16').pack()
 
root.mainloop() 
