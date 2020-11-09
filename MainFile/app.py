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
#keeps Unicode Dice Values
DICE = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
dice_rolled=[]
dice_kept=[]
score=IntVar()#total
points=IntVar()#current

for i in range(0, 6):
    dice_rolled.append(StringVar())
    dice_kept.append(StringVar())

# MessageBox on Close
#This triggers only if the player exits the game.
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing) # message box

def randomGen():
    forget()
    for i in range(0, 6):
        dice_rolled[i].set(random.choice(DICE))


#choose dice to keep in current points
def keep_dice(args):
    if dice_kept[args].get() == '':
        dice_kept[args].set(dice_rolled[args].get())
    else:
        dice_kept[args].set('')
    calc_pts()

#calculate your points given a particular set of dice
def calc_pts():
    temp_score = 0
    dice_count = [0] * 6
    for i in range(0, 6):
        if (dice_kept[i].get() == DICE[0]):
            dice_count[0] += 1
        if (dice_kept[i].get() == DICE[1]):
            dice_count[1] += 1
        if (dice_kept[i].get() == DICE[2]):
            dice_count[2] += 1
        if (dice_kept[i].get() == DICE[3]):
            dice_count[3] += 1
        if (dice_kept[i].get() == DICE[4]):
            dice_count[4] += 1
        if (dice_kept[i].get() == DICE[5]):
            dice_count[5] += 1

    temp_score += 100 * dice_count[0]  # Add 100 for each dice with value 1.
    temp_score += 50 * dice_count[4]  # Add 50 for each dice with value 5.
    straight_count = 0
    pair_count = 0
    # This for loop will count how many pairs or straights are there.
    for i in range(0, 6):
        if dice_count[i] == 1:
            straight_count += 1
        elif dice_count[i] == 2:
            pair_count += 1
        elif dice_count[i] > 2:
            if i == 0:
                temp_score += 1000 * (dice_count[i] - 2) - (100 * dice_count[i])
            elif i == 4:
                temp_score += 5 * 100 * (dice_count[i] - 2) - (50 * dice_count[i])
            else:
                temp_score += (i + 1) * 100 * (dice_count[i] - 2)

    if straight_count == 6:
        temp_score += 350  # Add 350 points if all 6 dice are a straight.
    if pair_count == 3:
        temp_score += 500  # Add 500 points if there are 3 pairs of dice.
        if dice_count[0] > 0:
            temp_score -= 100 * dice_count[0]  # Subtract 100 for each 1.
        if dice_count[4] > 0:
            temp_score -= 50 * dice_count[0]  # Subtract 50 for each 5.
    new_score = temp_score
    score.set(new_score)


# reset the dice 
def forget():
    for i in range(0, 6):
        dice_rolled[i].set("")
        dice_kept[i].set("")
    score.set(0)

def newWin1():
    win1 = Toplevel(root)
    forget()
    root.eval(f'tk::PlaceWindow {str(win1)} center') # center screen
    win1.title("One Player")
    win1.geometry("400x400")
    win1.config(bg="green")
    root.resizable(False, False)
    user41_btn = Button(win1, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    frame = Frame(win1)
    frame.pack()
    for i in range(0,6):
        ans = Button(frame, textvariable=dice_rolled[i], height=1, width=2, font=("Helvetica", 20), command=lambda i=i :keep_dice(i)).pack(side=LEFT)
    user41_btn = Button(win1, text="delete dice", height=3, width=20, bg="blue", fg="white", command= forget).pack(pady=10)
    score_lbl = Label(win1, textvariable=score, bg="black", fg="white", font=("Helvetica", 16)).pack()

def newWin2():
    forget()
    win2 = Toplevel(root)
    root.eval(f'tk::PlaceWindow {str(win2)} center') # center screen
    win2.title("Two Player")
    win2.geometry("400x400")
    win2.config(bg="green")
    root.resizable(False, False)
    user42_btn = Button(win2, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    frame = Frame(win2)
    frame.pack()
    for i in range(0,6):
        ans = Button(frame, textvariable=dice_rolled[i], height=1, width=2, font=("Helvetica", 20), command=lambda i=i :keep_dice(i)).pack(side=LEFT)
    user42_btn = Button(win2, text="delete dice", height=3, width=20, bg="blue", fg="white", command= forget).pack(pady=10)
    score_lbl = Label(win2, textvariable=score, bg="black", fg="white", font=("Helvetica", 16)).pack()

def newWin3():
    win3 = Toplevel(root)
    forget()
    root.eval(f'tk::PlaceWindow {str(win3)} center') # center screen
    win3.title("Three Player")
    win3.geometry("400x400")
    win3.config(bg="green")
    root.resizable(False, False)
    user43_btn = Button(win3, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    frame = Frame(win3)
    frame.pack()
    for i in range(0,6):
        ans = Button(frame, textvariable=dice_rolled[i], height=1, width=2, font=("Helvetica", 20), command=lambda i=i :keep_dice(i)).pack(side=LEFT)
    user43_btn = Button(win3, text="delete dice", height=3, width=20, bg="blue", fg="white", command= forget).pack(pady=10)
    score_lbl = Label(win3, textvariable=score, bg="black", fg="white", font=("Helvetica", 16)).pack()

# Varaiables with location
title_lbl = Label(root, text="10,000", fg="white", bg="black", font=("Helvetica", 16)).pack()
player_lbl = Label(root, text="Select the Number of Players", fg="white", bg="black", font=("Helvetica", 16)).pack()
user1_btn = Button(root, text="one", height=3, width=20, bg="blue", fg="white", command=newWin1).pack(pady=10)
user2_btn = Button(root, text="two", height=3, width=20, bg="blue", fg="white", command=newWin2).pack(pady=10)
user3_btn = Button(root, text="three", height=3, width=20, bg="blue", fg="white", command=newWin3).pack(pady=10)
quit_btn = Button(root, text="quit", height=3, width=20, bg="blue", fg="white", command=on_closing).pack(pady=10)
#user4_btn = Button(root, text="change me", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
#result_lbl = Label(root, textvariable=stringme, bg="black", fg="white", font=("Helvetica", 30)).pack()
#score_lbl = Label(root, textvariable=score, bg="black", fg="white", font=("Helvetica", 30)).pack()

root.mainloop()
