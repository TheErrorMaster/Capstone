from tkinter import *
import random

#Window variables
root = Tk()
root.title('10,000 Dice')
root.geometry("400x400")
root.config(bg="black")
dice_set = StringVar()
score = IntVar()

# Functions
def randomGen():
    ls = []
    #See below for the dice unicode:
    #'\u2680' = dice-one
    #'\u2681' = dice-two
    #'\u2682' = dice-three
    #'\u2683' = dice-four
    #'\u2684' = dice-five
    #'\u2685' = dice-six
    tmpscore = 0
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dice_count = [0]*6
    for i in range(0,6):
        # ls.append(random.randrange(1,6)) # list of rand int
        ls.append(random.choice(dice))
        if (ls[i] == '\u2680'):
            dice_count[0] += 1
        if (ls[i] == '\u2681'):
            dice_count[1] += 1
        if (ls[i] == '\u2682'):
            dice_count[2] += 1
        if (ls[i] == '\u2683'):
            dice_count[3] += 1
        if (ls[i] == '\u2684'):
            dice_count[4] += 1
        if (ls[i] == '\u2685'):
            dice_count[5] += 1

    tmpscore += 100*dice_count[0]
    tmpscore += 50*dice_count[4]
    straight_count = 0
    pair_count = 0
    for i in range(0,6):
        if dice_count[i] == 1:
            straight_count += 1
        if dice_count[i] == 2:
            pair_count += 1
        if dice_count[i] > 2:
            if i == 0:
                tmpscore += 1000 * (dice_count[i] - 2) - 100*dice_count[i]
            elif i == 4:
                tmpscore += 5 * 100 * (dice_count[i] - 2) - 50*dice_count[i]
            else:
                tmpscore += (i + 1) * 100 * (dice_count[i] - 2)

    if straight_count == 6:
        tmpscore += 350
    if pair_count == 3:
        tmpscore += 500
        if dice_count[0] > 0:
            tmpscore -= 100*dice_count[0]
        if dice_count[4] > 0:
            tmpscore -= 50*dice_count[4]

    lis = " ".join(map(str,ls)) # list to string
    dice_set.set(lis)
    new_score = tmpscore
    score.set(new_score)

# Variables
title_lbl = Label(root, text="10,000", fg="white", bg="black", font=("Helvetica", 16))
player_lbl = Label(root, text="Select the Number of Players", fg="white", bg="black", font=("Helvetica", 16))
user1_btn = Button(root, text="one", height=3, width=20, bg="blue", fg="white")
user2_btn = Button(root, text="two", height=3, width=20, bg="blue", fg="white")
user3_btn = Button(root, text="Roll the dice", height=3, width=20, bg="blue", fg="white", command=randomGen)
result_lbl = Label(root, textvariable=dice_set, bg="black", fg="white", font=("Helvetica", 30))
score_lbl = Label(root, textvariable=score, fg="white", bg="black", font=("Helvetica", 16))

# Location
title_lbl.pack()
player_lbl.pack()
user1_btn.pack(pady=(10)) # horizontal padding between buttons
user2_btn.pack(pady=(10))
user3_btn.pack(pady=(10))
result_lbl.pack()
score_lbl.pack()


root.mainloop()
