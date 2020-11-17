from tkinter import *
from tkinter import messagebox #Needed for exit function.
import random

#Window variables
root = Tk()
root.title('tk::PlaceWindow . center')
root.title('10,000 Dice')
root.geometry("400x500")
root.config(bg="green")
root.resizable(False, False) #Disallow players from resizing the window.
stringme=StringVar()
pointsPlayer=IntVar() # the current amount of points for the player
totalPlayer=IntVar() #the total amount of points for the player
pointsAI=IntVar() # the current amount of points for the AI
totalAI=IntVar() #the total amount of points for the AI
playerTurn = True #Determine who's turn is it

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
        dice_rolled[i].set(random.choice(dice))

def keep_dice(args):
    if dice_kept[args].get() == '':
        dice_kept[args].set(dice_rolled[args].get())
    else:
        dice_kept[args].set('')
    calc_points()
        
def calc_points():
    temp_score = 0
    new_total = totalPlayer.get()
    dice_count = [0] * 6
    for i in range(0, 6):
        if (dice_kept[i].get() == dice[0]):
            dice_count[0] += 1
        if (dice_kept[i].get() == dice[1]):
            dice_count[1] += 1
        if (dice_kept[i].get() == dice[2]):
            dice_count[2] += 1
        if (dice_kept[i].get() == dice[3]):
            dice_count[3] += 1
        if (dice_kept[i].get() == dice[4]):
            dice_count[4] += 1
        if (dice_kept[i].get() == dice[5]):
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
    
    new_score = temp_score
    pointsPlayer.set(new_score)
##    #Display this message box below only if the player can't score.
##    if points.get() == 0:
##        messagebox.showinfo("info", "No Points left, End of turn")
##    else:
##        new_total = total.get() + points.get()
##        total.set(new_total)
    new_total = totalPlayer.get() + pointsPlayer.get()
    totalPlayer.set(new_total)

    # Is the total number of points greater than or equal to 10000?
    # If yes, then display the winning message.
    if (totalPlayer.get() >= 10000):
        messagebox.showinfo("info", "You won!")

#This function will have the AI player score points by rolling the dice.
def aiTurn():
    randomGen()
    temp_score = 0
    new_total = totalAI.get()
    dice_count = [0] * 6
    for i in range(0, 6):
        if (dice_kept[i].get() == dice[0]):
            dice_count[0] += 1
        if (dice_kept[i].get() == dice[1]):
            dice_count[1] += 1
        if (dice_kept[i].get() == dice[2]):
            dice_count[2] += 1
        if (dice_kept[i].get() == dice[3]):
            dice_count[3] += 1
        if (dice_kept[i].get() == dice[4]):
            dice_count[4] += 1
        if (dice_kept[i].get() == dice[5]):
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
    
    new_score = temp_score
    pointsAI.set(new_score)
##    #Display this message box below only if the player can't score.
##    if points.get() == 0:
##        messagebox.showinfo("info", "No Points left, End of turn")
##    else:
##        new_total = total.get() + points.get()
##        total.set(new_total)
    new_total = totalAI.get() + pointsAI.get()
    totalAI.set(new_total)

    # Is the total number of points greater than or equal to 10000?
    # If yes, then display the losing message.
    if (totalAI.get() >= 10000):
        messagebox.showinfo("info", "Sorry, you lost!")
        
#Reset sets all values to default, including the total amount of points.
def reset():
    for i in range(0, 6):
        dice_rolled[i].set("")
        dice_kept[i].set("")
    pointsPlayer.set(0)
    totalPlayer.set(0)
    pointsAI.set(0)
    totalAI.set(0)

#Forget is like reset, except it only keeps the total amount of points.
def forget():
    for i in range(0, 6):
        dice_rolled[i].set("")
        dice_kept[i].set("")
    pointsPlayer.set(0)
    pointsAI.set(0)

def newWin1():
    win1 = Toplevel(root)
    forget()
    root.eval(f'tk::PlaceWindow {str(win1)} center') # center screen
    win1.title("One Player")
    win1.geometry("450x600")
    win1.config(bg="green")
    win1.resizable(False, False)
    roll_btn = Button(win1, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    frame = Frame(win1)
    frame.pack()
    for i in range(0, 6):
        ans = Button(frame, textvariable=dice_rolled[i], height=1, width=2, font=("Helvetica", 20), command=lambda i=i : keep_dice(i)).pack(side=LEFT)
    result_lbls = Label(win1, textvariable=stringme, bg="green", fg="white", font=("Helvetica", 30)).pack()
    endTurn_btn = Button(win1, text="End Turn", height=3, width=20, bg="blue", fg="white", command=aiTurn).pack(pady=10)
    reset_btn = Button(win1, text="Reset", height=3, width=20, bg="blue", fg="white", command=reset).pack(pady=10)
    #score_player_text = Label(win1, textvariable="Your Points", bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    score_player_lbl = Label(win1, textvariable=pointsPlayer, bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    #total_player_text = Label(win1, textvariable="Your Total Points", bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    total_player_lbl = Label(win1, textvariable=totalPlayer, bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    #score_ai_text = Label(win1, textvariable="AI's Points", bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    score_ai_lbl = Label(win1, textvariable=pointsAI, bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    #total_ai_text = Label(win1, textvariable="AI's Total Points", bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    total_ai_lbl = Label(win1, textvariable=totalAI, bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)

def newWin2():
    forget()
    win2 = Toplevel(root)
    root.eval(f'tk::PlaceWindow {str(win2)} center') # center screen
    win2.title("Two Player")
    win2.geometry("450x600")
    win2.config(bg="green")
    win2.resizable(False, False)
    roll_btn = Button(win2, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    frame = Frame(win1)
    frame.pack()
    for i in range(0, 6):
        ans = Button(frame, textvariable=dice_rolled[i], height=1, width=2, font=("Helvetica", 20), command=lambda i=i : keep_dice(i)).pack(side=LEFT)
    result_lbls = Label(win2, textvariable=stringme, bg="green", fg="white", font=("Helvetica", 30)).pack()
    endTurn_btn = Button(win2, text="End Turn", height=3, width=20, bg="blue", fg="white", command=aiTurn).pack(pady=10)
    reset_btn = Button(win2, text="Reset", height=3, width=20, bg="blue", fg="white", command=reset).pack(pady=10)
    #score_player_text = Label(win2, textvariable="Your Points", bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    score_player_lbl = Label(win2, textvariable=pointsPlayer, bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    #total_player_text = Label(win2, textvariable="Your Total Points", bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    total_player_lbl = Label(win2, textvariable=totalPlayer, bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    #score_ai_text = Label(win2, textvariable="AI's Points", bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    score_ai_lbl = Label(win2, textvariable=pointsAI, bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    #total_ai_text = Label(win2, textvariable="AI's Total Points", bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    total_ai_lbl = Label(win2, textvariable=totalAI, bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)

def newWin3():
    win3 = Toplevel(root)
    forget()
    root.eval(f'tk::PlaceWindow {str(win3)} center') # center screen
    win3.title("Three Player")
    win3.geometry("450x600")
    win3.config(bg="green")
    win3.resizable(False, False)
    roll_btn = Button(win3, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    frame = Frame(win1)
    frame.pack()
    for i in range(0, 6):
        ans = Button(frame, textvariable=dice_rolled[i], height=1, width=2, font=("Helvetica", 20), command=lambda i=i : keep_dice(i)).pack(side=LEFT)
    result_lbls = Label(win1, textvariable=stringme, bg="green", fg="white", font=("Helvetica", 30)).pack()
    endTurn_btn = Button(win1, text="End Turn", height=3, width=20, bg="blue", fg="white", command=aiTurn).pack(pady=10)
    reset_btn = Button(win1, text="Reset", height=3, width=20, bg="blue", fg="white", command=reset).pack(pady=10)
    #score_player_text = Label(win3, textvariable="Your Points", bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    score_player_lbl = Label(win3, textvariable=pointsPlayer, bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    #total_player_text = Label(win3, textvariable="Your Total Points", bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    total_player_lbl = Label(win3, textvariable=totalPlayer, bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    #score_ai_text = Label(win3, textvariable="AI's Points", bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    score_ai_lbl = Label(win3, textvariable=pointsAI, bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    #total_ai_text = Label(win3, textvariable="AI's Total Points", bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)
    total_ai_lbl = Label(win3, textvariable=totalAI, bg="green", fg="white", font=("Helvetica", 16)).pack(pady=10)

# Varaiables with location
title_lbl = Label(root, text="10,000 Dice", fg="white", bg="green", font=("Helvetica", 16)).pack()
player_lbl = Label(root, text="Select the Number of Players", fg="white", bg="green", font=("Helvetica", 16)).pack()
user1_btn = Button(root, text="one", height=3, width=20, bg="blue", fg="white", command=newWin1).pack(pady=10)
user2_btn = Button(root, text="two", height=3, width=20, bg="blue", fg="white", command=newWin2).pack(pady=10)
user3_btn = Button(root, text="three", height=3, width=20, bg="blue", fg="white", command=newWin3).pack(pady=10)
quit_btn = Button(root, text="quit", height=3, width=20, bg="blue", fg="white", command=on_closing).pack(pady=10)

root.mainloop()
