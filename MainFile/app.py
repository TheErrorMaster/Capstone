from tkinter import *
from tkinter import messagebox #Needed for exit function.
import random

#Window variables
root = Tk()
root.title('tk::PlaceWindow . center')
root.title('10,000 Dice')
root.geometry("400x400")
root.config(bg="green")
root.resizable(False, False) #Disallow players from resizing the window.
stringme=StringVar()
score=IntVar()

# MessageBox on Close
#This triggers only if the player exits the game.
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing) # message box

def randomGen():
    ls = []
    temp_score = 0
    #See below for the dice unicode:
    #'\u2680' = dice-one
    #'\u2681' = dice-two
    #'\u2682' = dice-three
    #'\u2683' = dice-four
    #'\u2684' = dice-five
    #'\u2685' = dice-six
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    for i in range(6):
        # ls.append(random.randrange(1,6)) # list of rand int
        ls.append(random.choice(dice))
        if (random.choice(dice) == '\u2680'):
            temp_score += 1000
        if (random.choice(dice) == '\u2681'):
            temp_score += 200
        if (random.choice(dice) == '\u2682'):
            temp_score += 300
        if (random.choice(dice) == '\u2683'):
            temp_score += 400
        if (random.choice(dice) == '\u2684'):
            temp_score += 500
        if (random.choice(dice) == '\u2685'):
            temp_score += 600
    lis = " ".join(map(str,ls)) # list to string
    stringme.set(lis)
    new_score = temp_score
    score.set(new_score)

# reset the dice 
def forget():
    stringme.set("")
    score.set(0)

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
    score_lbl = Label(win1, textvariable=score, bg="black", fg="white", font=("Helvetica", 30)).pack()

def newWin2():
    forget()
    win2 = Toplevel(root)
    root.eval(f'tk::PlaceWindow {str(win2)} center') # center screen
    win2.title("Two Player")
    win2.geometry("400x400")
    win2.config(bg="black")
    user4_btn = Button(win2, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    result_lbls = Label(win2, textvariable=stringme, bg="black", fg="white", font=("Helvetica", 30)).pack()
    user42_btn = Button(win2, text="delete dice", height=3, width=20, bg="blue", fg="white", command= forget).pack(pady=10)
    score_lbl = Label(win2, textvariable=score, bg="black", fg="white", font=("Helvetica", 30)).pack()

def newWin3():
    win3 = Toplevel(root)
    forget()
    root.eval(f'tk::PlaceWindow {str(win3)} center') # center screen
    win3.title("Three Player")
    win3.geometry("400x400")
    win3.config(bg="black")
    user4_btn = Button(win3, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    result_lbls = Label(win3, textvariable=stringme, bg="black", fg="white", font=("Helvetica", 30)).pack()
    user43_btn = Button(win3, text="delete dice", height=3, width=20, bg="blue", fg="white", command= forget).pack(pady=10)
    score_lbl = Label(win3, textvariable=score, bg="black", fg="white", font=("Helvetica", 30)).pack()

# Varaiables with location
title_lbl = Label(root, text="10,000", fg="white", bg="black", font=("Helvetica", 16)).pack()
player_lbl = Label(root, text="Select the Number of Players", fg="white", bg="black", font=("Helvetica", 16)).pack()
user1_btn = Button(root, text="one", height=3, width=20, bg="blue", fg="white", command=newWin1).pack(pady=10)
user2_btn = Button(root, text="two", height=3, width=20, bg="blue", fg="white", command=newWin2).pack(pady=10)
user3_btn = Button(root, text="three", height=3, width=20, bg="blue", fg="white", command=newWin3).pack(pady=10)
#user4_btn = Button(root, text="change me", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
#result_lbl = Label(root, textvariable=stringme, bg="black", fg="white", font=("Helvetica", 30)).pack()
#score_lbl = Label(root, textvariable=score, bg="black", fg="white", font=("Helvetica", 30)).pack()

root.mainloop()
