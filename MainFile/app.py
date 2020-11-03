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

# MessageBox on Close
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing) # message box

def randomGen():
    ls = []
    #See below for the dice unicode:
    #'\u2680' = dice-one
    #'\u2681' = dice-two
    #'\u2682' = dice-three
    #'\u2683' = dice-four
    #'\u2684' = dice-five
    #'\u2685' = dice-six
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    for i in range(10):
        # ls.append(random.randrange(1,6)) # list of rand int
        ls.append(random.choice(dice))

    lis = " ".join(map(str,ls)) # list to string
    stringme.set(lis)

# reset dice 
def forget():
    stringme.set("")

def newWin1():
    win1 = Toplevel(root)
    forget()
    root.eval(f'tk::PlaceWindow {str(win1)} center') # center screen
    win1.title("One Player")
    win1.geometry("400x400")
    win1.config(bg="black")
    user41_btn = Button(win1, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    result_lblse = Label(win1, textvariable=stringme, bg="black", fg="white", font=("Helvetica", 30)).pack()
    user41_btn = Button(win1, text="delete dice", height=3, width=20, bg="blue", fg="white", command= forget).pack(pady=10)


def newWin2():
    forget()
    win2 = Toplevel(root)
    root.eval(f'tk::PlaceWindow {str(win2)} center') # center screen
    win2.title("Two Player")
    win2.geometry("400x400")
    win2.config(bg="black")
    user4_btn = Button(win2, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    result_lbls = Label(win2, textvariable=stringme, bg="black", fg="white", font=("Helvetica", 30)).pack()

def newWin3():
    win3 = Toplevel(root)
    forget()
    root.eval(f'tk::PlaceWindow {str(win3)} center') # center screen
    win3.title("Three Player")
    win3.geometry("400x400")
    win3.config(bg="black")
    user4_btn = Button(win3, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    result_lbls = Label(win3, textvariable=stringme, bg="black", fg="white", font=("Helvetica", 30)).pack()

# Varaiables
title_lbl = Label(root, text="10,000", fg="white", bg="black", font=("Helvetica", 16)).pack()
player_lbl = Label(root, text="Select the Number of Players", fg="white", bg="black", font=("Helvetica", 16)).pack() # horizontal padding between buttons
user1_btn = Button(root, text="one", height=3, width=20, bg="blue", fg="white", command=newWin1).pack(pady=10)
user2_btn = Button(root, text="two", height=3, width=20, bg="blue", fg="white", command=newWin2).pack(pady=10)
user3_btn = Button(root, text="three", height=3, width=20, bg="blue", fg="white", command=newWin3).pack(pady=10)
# user4_btn = Button(root, text="change me", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
# result_lbls = Label(root, textvariable=stringme, bg="black", fg="white", font=("Helvetica", 30)).pack()

root.mainloop()