import random
from tkinter import *
import pyperclip as pc

def passwordgenerator():
    s="ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"                #string which stores all the characters
    passw=[]
    len_passw=int(p.get())
    for x in range(0,int(len_passw)):
        passw.append(random.choices(s)[0])                                          #we generate a random character from the string s
    passclip="".join(passw)                                                         #join the generated characters to a string
    Label(window,text="The suggested password is :").place(x=0,y=115)
    Label(window,text=passclip).place(x=160,y=115)
    copy=Button(window,text="Copy to clipboard",command=lambda: copyclip(passclip)).place(x=110,y=150)
def copyclip(a):                                                                    #function to copy the generated password to clipboard
    pc.copy(a)
    

window=Tk()
window.configure(bg="blue")
window.title("Password Generator")
window.geometry("300x300")
Label(window,text="Password Generator",bg="blue",fg="red",font="Arial").place(x=75,y=0)
Label(window,text="Enter the length of the password to be generated :",bg="blue",fg="red",bd=5).place(x=15,y=30)
p=StringVar()
Entry(window,textvariable=p).place(x=80,y=60)
calci=Button(window,text="Generate",command=lambda: passwordgenerator()).place(x=115,y=85)

