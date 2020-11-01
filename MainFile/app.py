from tkinter import *
import random

#Window variables
root = Tk()
root.title('10,000 Dice')
root.geometry("400x400")
root.config(bg="green")
stringme=StringVar()
score=IntVar()

# Functions
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

# Varaiables
title_lbl = Label(root, text="10,000", fg="white", bg="black", font=("Helvetica", 16))
player_lbl = Label(root, text="Select the Number of Players", fg="white", bg="black", font=("Helvetica", 16))
user1_btn = Button(root, text="one", height=3, width=20, bg="blue", fg="white")
user2_btn = Button(root, text="two", height=3, width=20, bg="blue", fg="white")
user3_btn = Button(root, text="change me", height=3, width=20, bg="blue", fg="white", command=randomGen)
result_lbl = Label(root, textvariable=stringme, bg="black", fg="white", font=("Helvetica", 30))
score_lbl = Label(root, textvariable=score, bg="black", fg="white", font=("Helvetica", 30))

# Location
title_lbl.pack()
player_lbl.pack()
user1_btn.pack(pady=(10)) # horizontal padding between buttons
user2_btn.pack(pady=(10))
user3_btn.pack(pady=(10))
result_lbl.pack()
score_lbl.pack()

root.mainloop()
