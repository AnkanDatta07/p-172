# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 11:32:30 2023

@author: Ankan Datta
"""

from tkinter import * 
root = Tk()
root.title("Inheritence")
root.geometry("700x700")
root.configure(bg = "cyan")

label1 = Label(root, text = "User Name: ")
label1.place(relx = 0.4, rely = 0.4, anchor = CENTER)
label2 = Label(root, text = "Email Id: ")
label2.place(relx = 0.4, rely = 0.5, anchor = CENTER)

user1 = Entry(root)
user1.place(relx = 0.6, rely = 0.4, anchor = CENTER)
email = Entry(root)
email.place(relx = 0.6, rely = 0.5, anchor = CENTER)

label_header = Label(root, text = "INHERITENCE", bg = "lightpink", fg = "red",font=("Arial", 60))
label_header.place(relx = 0.51, rely = 0.2, anchor = CENTER)

labelfooter = Label(root, text = "Made By Ankan Datta[whitehatjr.]", bg = "lightpink", fg = "red")
labelfooter.place(relx = 0.51, rely = 0.9, anchor=CENTER)

class User:
         
    def addUser(key, value):
        global dictionary
        dictionary[key] = value
        label0["text"] = dictionary
            
class Getuser(User):
    def getuser(self):
        us = user1.get()
        em = email.get()
        User.addUser(us, em)
    
user = Getuser()

btn1 = Button(root, text = "Add User Details", bg = "lightgreen", fg = "black", command = user.getuser)
btn1.place(relx = 0.5, rely = 0.6, anchor = CENTER)

label0 = Label(root)
label0.place(relx = 0.5, rely = 0.7, anchor = CENTER)

dictionary = {}

root.mainloop()