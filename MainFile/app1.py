from tkinter import *
from tkinter import messagebox
import random

#Window variables
root = Tk()
root.eval('tk::PlaceWindow . center') # center screen
root.title('10,000 Dice')
root.geometry("400x400")
root.config(bg="black")
stringme=StringVar()

def randomGen():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    for i in range(10):
        ans = Button(root, text=random.choice(dice), height=2, width=2, font=("Helvetica", 15)).pack(side=LEFT)



player_lbl = Label(root, text="Select the Number of Players", fg="white", bg="black", font=("Helvetica", 16)).pack() # horizontal padding between buttons
user4_btn = Button(root, text="change me", height=3, width=10, bg="blue", fg="white", command=randomGen).pack()

root.mainloop()