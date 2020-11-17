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
dice_btns = []
curr_pts = 0
points=IntVar() # the current amount of points
total=IntVar() #the total amount of points

#See below for the dice unicode:
#'\u2680' = dice-one
#'\u2681' = dice-two
#'\u2682' = dice-three
#'\u2683' = dice-four
#'\u2684' = dice-five
#'\u2685' = dice-six
dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

dice_rolled=[]
dice_kept=[]
curr_dice=[]

for i in range(0, 6):
    dice_rolled.append(StringVar())
    dice_kept.append(StringVar())
    curr_dice.append(StringVar())

# MessageBox on Close
#This triggers only if the player exits the game.
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing) # message box

def randomGen():
    forget()
    for i in range(0, 6):
        dice_rolled[i].set(random.choice(dice))

def keep_dice(args):
    current_score = calc_points()
    button = dice_btns[args]
    #add dice to score if unadded
    if dice_kept[args].get() == '' and curr_dice[args].get() == '':
        curr_dice[args].set(dice_rolled[args].get())
        #only add dice if points are available
        if current_score == calc_points():
            curr_dice[args].set('')
        else:
            button.config(relief=SUNKEN)
    #take dice from score if already added
    elif dice_kept == '':
        curr_dice[args].set('')
        button.config(relief=RAISED)
    curr_pts = calc_points()
    points.set(points.get()-current_score+curr_pts)

    for i in range(0, 6):
        if dice_kept[i].get() == '':
            return
    #reset dice and continue to roll

        
def calc_points():
    temp_score = 0
    dice_count = [0] * 6
    for i in range(0, 6):
        if (curr_dice[i].get() == dice[0]):
            dice_count[0] += 1
        if (curr_dice[i].get() == dice[1]):
            dice_count[1] += 1
        if (curr_dice[i].get() == dice[2]):
            dice_count[2] += 1
        if (curr_dice[i].get() == dice[3]):
            dice_count[3] += 1
        if (curr_dice[i].get() == dice[4]):
            dice_count[4] += 1
        if (curr_dice[i].get() == dice[5]):
            dice_count[5] += 1

    temp_score += 100 * dice_count[0] #Add 100 for each dice with value 1.
    temp_score += 50 * dice_count[4] #Add 50 for each dice with value 5.
    straight_count = 0
    pair_count = 0
    #This for loop will count how many pairs or straights are there.
    for i in range(0,6):
        if dice_count[i] == 1:
            straight_count += 1
        elif dice_count[i] == 2:
            pair_count += 1
        elif dice_count[i] > 2:
            if i == 0:
                temp_score += 1000 * (dice_count[i]-2) - (100*dice_count[i])
            elif i == 4:
                temp_score += 5 * 100 * (dice_count[i]-2) - (50*dice_count[i])
            else:
                temp_score += (i+1) * 100 * (dice_count[i]-2)

    if straight_count == 6:
        temp_score += 350 #Add 350 points if all 6 dice are a straight.
    if pair_count == 3:
        temp_score += 500 #Add 500 points if there are 3 pairs of dice.
        if dice_count[0] > 0:
            temp_score -= 100 * dice_count[0] #Subtract 100 for each 1.
        if dice_count[4] > 0:
            temp_score -= 50 * dice_count[0] #Subtract 50 for each 5.
    return temp_score
##    #Display this message box below only if the player can't score.
##    if points.get() == 0:
##        messagebox.showinfo("info", "No Points left, End of turn")
##    else:
##        new_total = total.get() + points.get()
##        total.set(new_total)

def reroll():
    for i in range(0, 6):
        if  curr_dice[i].get() != '':
            dice_kept[i].set(curr_dice[i].get())
        if dice_kept[i].get() == '':
            dice_rolled[i].set(random.choice(dice))

def endTurn():
    new_total = total.get() + points.get()
    total.set(new_total)

    # Is the total number of points greater than or equal to 10000?
    # If yes, then display the winning message.
    if (total.get() >= 10000):
        messagebox.showinfo("info", "You won!")
    forget()

        
#Reset sets all values to default, including the total amount of points.
def reset():
    for i in range(0, 6):
        dice_rolled[i].set("")
        dice_kept[i].set("")
        curr_dice[i].set("")
        dice_btns[i].config(relief=RAISED)
    points.set(0)
    total.set(0)

#Forget is like reset, except it only keeps the total amount of points.
def forget():
    for i in range(0, 6):
        dice_rolled[i].set("")
        dice_kept[i].set("")
        curr_dice[i].set("")
        if len(dice_btns) != 0:
            dice_btns[i].config(relief=RAISED)
    points.set(0)

def newWin1():
    win1 = Toplevel(root)
    forget()
    root.eval(f'tk::PlaceWindow {str(win1)} center') # center screen
    win1.title("One Player")
    win1.geometry("450x450")
    win1.config(bg="green")
    win1.resizable(False, False)
    roll_btn = Button(win1, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)

    #DICE
    frame = Frame(win1)
    frame.pack()
    for i in range(0, 6):
        ans = Button(frame, textvariable=dice_rolled[i], height=1, width=2, font=("Helvetica", 20), command=lambda i=i : keep_dice(i))
        ans.pack(side=LEFT)
        dice_btns.append(ans)
    result_lbls = Label(win1, textvariable=stringme, bg="green", fg="white", font=("Helvetica", 30)).pack()

    #TURN OPTIONS
    frame2 = Frame(win1, bg = "green")
    frame2.pack()
    rollon_btn = Button(frame2, text="Keep points and \nRoll the remaining dice", height=3, width=20, bg="blue", fg="white", command=reroll)
    rollon_btn.pack(side=LEFT)
    rollon_btn.pack(padx=10)
    endturn_btn = Button(frame2, text="End Turn and \nAdd Points to Score", height=3, width=20, bg="blue", fg="white", command=endTurn)
    endturn_btn.pack(padx=10)
    endturn_btn.pack(side=LEFT)

    #SCOREBOARD
    score_lbl = Label(win1, textvariable=points, bg="green", fg="white", font=("Helvetica", 16)).pack()
    total_lbl = Label(win1, textvariable=total, bg="green", fg="white", font=("Helvetica", 16)).pack()
    reset_btn = Button(win1, text="reset", height=3, width=20, bg="blue", fg="white", command=reset).pack(pady=10)

def newWin2():
    forget()
    win2 = Toplevel(root)
    root.eval(f'tk::PlaceWindow {str(win2)} center') # center screen
    win2.title("Two Player")
    win2.geometry("450x450")
    win2.config(bg="green")
    win2.resizable(False, False)
    roll_btn = Button(win2, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    frame = Frame(win1)
    frame.pack()
    for i in range(0, 6):
        ans = Button(frame, textvariable=dice_rolled[i], height=1, width=2, font=("Helvetica", 20), command=lambda i=i : keep_dice(i)).pack(side=LEFT)
    result_lbls = Label(win2, textvariable=stringme, bg="green", fg="white", font=("Helvetica", 30)).pack()
    reset_btn = Button(win2, text="reset", height=3, width=20, bg="blue", fg="white", command=reset).pack(pady=10)
    score_lbl = Label(win2, textvariable=points, bg="green", fg="white", font=("Helvetica", 16)).pack()
    total_lbl = Label(win2, textvariable=total, bg="green", fg="white", font=("Helvetica", 16)).pack()

def newWin3():
    win3 = Toplevel(root)
    forget()
    root.eval(f'tk::PlaceWindow {str(win3)} center') # center screen
    win3.title("Three Player")
    win3.geometry("450x450")
    win3.config(bg="green")
    win3.resizable(False, False)
    roll_btn = Button(win3, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    frame = Frame(win1)
    frame.pack()
    for i in range(0, 6):
        ans = Button(frame, textvariable=dice_rolled[i], height=1, width=2, font=("Helvetica", 20), command=lambda i=i : keep_dice(i)).pack(side=LEFT)
    result_lbls = Label(win3, textvariable=stringme, bg="green", fg="white", font=("Helvetica", 30)).pack()
    reset_btn = Button(win3, text="reset", height=3, width=20, bg="blue", fg="white", command=reset).pack(pady=10)
    score_lbl = Label(win3, textvariable=points, bg="green", fg="white", font=("Helvetica", 16)).pack()
    total_lbl = Label(win3, textvariable=total, bg="green", fg="white", font=("Helvetica", 16)).pack()

# Varaiables with location
title_lbl = Label(root, text="10,000 Dice", fg="white", bg="green", font=("Helvetica", 16)).pack()
player_lbl = Label(root, text="Select the Number of Players", fg="white", bg="green", font=("Helvetica", 16)).pack()
user1_btn = Button(root, text="one", height=3, width=20, bg="blue", fg="white", command=newWin1).pack(pady=10)
user2_btn = Button(root, text="two", height=3, width=20, bg="blue", fg="white", command=newWin2).pack(pady=10)
user3_btn = Button(root, text="three", height=3, width=20, bg="blue", fg="white", command=newWin3).pack(pady=10)
quit_btn = Button(root, text="quit", height=3, width=20, bg="blue", fg="white", command=on_closing).pack(pady=10)

root.mainloop()
