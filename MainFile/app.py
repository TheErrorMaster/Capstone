from tkinter import *
from tkinter import messagebox #Needed for exit function.
import random
import time

#Window variables
root = Tk()
root.title('tk::PlaceWindow . center')
root.title('10,000 Dice')
root.geometry("400x500")
root.config(bg="green")
root.resizable(False, False) #Disallow players from resizing the window.
dice_btns = []
curr_pts = IntVar()
points=IntVar() # the current amount of points
total=IntVar() #the total amount of points
pointsAI=IntVar()
totalAI=IntVar()

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
dice_count=[0] * 6

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

    #dice_count = [0] * 6
    for i in range(0, 6):
        if (dice_rolled[i].get() == dice[0]):
            dice_count[0] += 1
        if (dice_rolled[i].get() == dice[1]):
            dice_count[1] += 1
        if (dice_rolled[i].get() == dice[2]):
            dice_count[2] += 1
        if (dice_rolled[i].get() == dice[3]):
            dice_count[3] += 1
        if (dice_rolled[i].get() == dice[4]):
            dice_count[4] += 1
        if (dice_rolled[i].get() == dice[5]):
            dice_count[5] += 1

def keep_dice(args):#counts dice overall to test for 3s
    current_score = calc_points()
    button = dice_btns[args]
    #add dice to score if unadded
    if dice_kept[args].get() == '' and curr_dice[args].get() == '':
        curr_dice[args].set(dice_rolled[args].get())
        button.config(relief=SUNKEN)
    #take dice from score if already added
    elif dice_kept[args].get() == '':
        curr_dice[args].set('')
        button.config(relief=RAISED)
    curr = calc_points()
    points.set(points.get()-current_score+curr)
    #reset dice and continue to roll

def is_triple_position(arg):
    face = 0
    if (dice_rolled[arg].get() == dice[0]):
        face = 0
    if (dice_rolled[arg].get() == dice[1]):
        face = 1
    if (dice_rolled[arg].get() == dice[2]):
        face = 2
    if (dice_rolled[arg].get() == dice[3]):
        face = 3
    if (dice_rolled[arg].get() == dice[4]):
        face = 4
    if (dice_rolled[arg].get() == dice[5]):
        face = 5
    return dice_count[face] > 2
        
def calc_points():#counts dice for current for points
    temp_score = 0
    curr_dice_count = [0] * 6
    for i in range(0, 6):
        if (curr_dice[i].get() == dice[0]):
            curr_dice_count[0] += 1
        if (curr_dice[i].get() == dice[1]):
            curr_dice_count[1] += 1
        if (curr_dice[i].get() == dice[2]):
            curr_dice_count[2] += 1
        if (curr_dice[i].get() == dice[3]):
            curr_dice_count[3] += 1
        if (curr_dice[i].get() == dice[4]):
            curr_dice_count[4] += 1
        if (curr_dice[i].get() == dice[5]):
            curr_dice_count[5] += 1
    temp_score += 100 * curr_dice_count[0] #Add 100 for each dice with value 1.
    temp_score += 50 * curr_dice_count[4] #Add 50 for each dice with value 5.
    straight_count = 0
    pair_count = 0
    #This for loop will count how many pairs or straights are there.
    for i in range(0,6):
        if curr_dice_count[i] == 1:
            straight_count += 1
        elif curr_dice_count[i] == 2:
            pair_count += 1
        elif curr_dice_count[i] > 2:
            if i == 0:
                temp_score += 1000 * (curr_dice_count[i]-2) - (100*curr_dice_count[i])
            elif i == 4:
                temp_score += 5 * 100 * (curr_dice_count[i]-2) - (50*curr_dice_count[i])
            else:
                temp_score += (i+1) * 100 * (curr_dice_count[i]-2)

    if straight_count == 6:
        temp_score += 350 #Add 350 points if all 6 dice are a straight.
    if pair_count == 3:
        temp_score += 500 #Add 500 points if there are 3 pairs of dice.
        if curr_dice_count[0] > 0:
            temp_score -= 100 * curr_dice_count[0] #Subtract 100 for each 1.
        if curr_dice_count[4] > 0:
            temp_score -= 50 * curr_dice_count[0] #Subtract 50 for each 5.
    return temp_score
##    #Display this message box below only if the player can't score.
##    if points.get() == 0:
##        messagebox.showinfo("info", "No Points left, End of turn")
##    else:
##        new_total = total.get() + points.get()
##        total.set(new_total)

def reroll():
    count=0
    #Reroll only the dice that are not chosen yet.
    for i in range(0, 6):
        if curr_dice[i].get() != '':#add chosen dice to keep set
            dice_kept[i].set(curr_dice[i].get())
        if dice_kept[i].get() != '':#check for full chosen dice
            count+=1
        if dice_kept[i].get() == '':#reset only the unkept dice
            dice_rolled[i].set(random.choice(dice))
            
    #if all dice have been kept, then reset curr and kept,
    #and rolled to indicate none of the points.
    if count == 6:
        curr_pts.set(points.get())#Keep track of current points.
        randomGen()


    for i in range(0, 6):#no points? then turn end and no points received
        if dice_kept[i].get() == '':
            curr_dice[i].set(dice_rolled[i].get())
    pts = points.get()
    cal = calc_points()#somehow current dice are not being accounted for even while added, check loop above or calc meth
    if points.get()-calc_points() == 0:
        calc_points()
    pts=points.get()
    clc=calc_points()
    cur=curr_pts.get()
    if points.get()-calc_points()-curr_pts.get() == 0:
        #Display the message to indicate the player can't score points.
        messagebox.showinfo("info", "Sorry, no points earned, End of turn")
        points.set(0)
        endTurn()
    else:
        for i in range(0, 6):
            if dice_kept[i].get() == '':
                curr_dice[i].set('')


def endTurn():
    new_total = total.get() + points.get()
    total.set(new_total)
    points.set(0)

    # Is the total number of points greater than or equal to 10000?
    # If yes, then display the winning message.
    if (total.get() >= 10000):
        messagebox.showinfo("info", "You won!")
    forget()
    AITurn()

def AITurn():
    #initial roll
    randomGen()
    root.update()
    time.sleep(3)
    zero = False
    while TRUE:
        #scoring
        temp_score = 0
        temp_score += 100 * dice_count[0]  # Add 100 for each dice with value 1.
        temp_score += 50 * dice_count[4]  # Add 50 for each dice with value 5.
        straight_count = 0
        pair_count = 0
        ls = []
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
                ls.append(i); #include all triples or more

        if straight_count == 6:
            temp_score += 350  # Add 350 points if all 6 dice are a straight.
        if pair_count == 3:
            temp_score += 500  # Add 500 points if there are 3 pairs of dice.
            if dice_count[0] > 0:
                temp_score -= 100 * dice_count[0]  # Subtract 100 for each 1.
            if dice_count[4] > 0:
                temp_score -= 50 * dice_count[0]  # Subtract 50 for each 5.
        if temp_score == 0:
            zero = True
        pointsAI.set(pointsAI.get()+temp_score)

        #keeping dice
        keptcount=0
        for i in range(0, 6):
            button = dice_btns[i]
            if dice_rolled[i].get() == dice[0] or dice_rolled[i].get() == dice[4]:
                curr_dice[i].set(dice_rolled[i].get())
                button.config(relief=SUNKEN)
            if len(ls) == 1 and dice_rolled[i].get() == dice[ls[0]]:
                curr_dice[i].set(dice_rolled[i].get())
                button.config(relief=SUNKEN)
            if len(ls) == 2 and (dice_rolled[i].get() == dice[ls[0]] or dice_rolled[i].get() == dice[ls[1]]):
                curr_dice[i].set(dice_rolled[i].get())
                button.config(relief=SUNKEN)
            if curr_dice[i].get() != "":
                keptcount+=1;
            dice_count[i] = 0
        root.update()
        time.sleep(3)

        #reroll or endturn
        if keptcount < 4 and not zero:
            count = 0
            # Reroll only the dice that are not chosen yet.
            for i in range(0, 6):
                if curr_dice[i].get() != '':  # add chosen dice to keep set
                    dice_kept[i].set(curr_dice[i].get())
                if dice_kept[i].get() != '':  # check for full chosen dice
                    count += 1
                if dice_kept[i].get() == '':  # reset only the unkept dice
                    dice_rolled[i].set(random.choice(dice))

            # recalc dice_count
            for i in range(0, 6):
                if curr_dice[i].get() == '':
                    if (dice_rolled[i].get() == dice[0]):
                        dice_count[0] += 1
                    if (dice_rolled[i].get() == dice[1]):
                        dice_count[1] += 1
                    if (dice_rolled[i].get() == dice[2]):
                        dice_count[2] += 1
                    if (dice_rolled[i].get() == dice[3]):
                        dice_count[3] += 1
                    if (dice_rolled[i].get() == dice[4]):
                        dice_count[4] += 1
                    if (dice_rolled[i].get() == dice[5]):
                        dice_count[5] += 1
            # if all dice have been kept, then reset curr and kept,
            # and rolled to indicate none of the points.
            if count == 6:
                curr_pts.set(points.get())  # Keep track of current points.
                randomGen()
            root.update()
            time.sleep(3)
        else:
            totalAI.set(totalAI.get()+pointsAI.get())
            pointsAI.set(0)
            if (totalAI.get() >= 10000):
                messagebox.showinfo("info", "You Lost!")
            forget()
            return


        
#Reset sets all values to default, including the total amount of points.
def reset():
    for i in range(0, 6):
        dice_rolled[i].set("")
        dice_kept[i].set("")
        curr_dice[i].set("")
        if len(dice_btns) != 0:
            dice_btns[i].config(relief=RAISED)
    points.set(0)
    total.set(0)
    pointsAI.set(0)
    totalAI.set(0)

#Forget resets only the dice
def forget():
    for i in range(0, 6):
        dice_count[i] = 0
        dice_rolled[i].set("")
        dice_kept[i].set("")
        curr_dice[i].set("")
        if len(dice_btns) != 0:
            dice_btns[i].config(relief=RAISED)

def newWin1():
    win1 = Toplevel(root)
    reset()
    root.eval(f'tk::PlaceWindow {str(win1)} center') # center screen
    win1.title("One Player")
    win1.geometry("450x600")
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
    player_lbl = Label(win1, text="Player's points", bg="green", fg="white", font=("Helvetica", 16)).pack()
    score_lbl = Label(win1, textvariable=points, bg="green", fg="white", font=("Helvetica", 16)).pack()
    player2_lbl = Label(win1, text="Player's total", bg="green", fg="white", font=("Helvetica", 16)).pack()
    total_lbl = Label(win1, textvariable=total, bg="green", fg="white", font=("Helvetica", 16)).pack()
    AI_lbl = Label(win1, text="AI's points", bg="green", fg="white", font=("Helvetica", 16)).pack()
    scoreAI_lbl = Label(win1, textvariable=pointsAI, bg="green", fg="white", font=("Helvetica", 16)).pack()
    AI2_lbl = Label(win1, text="AI's total", bg="green", fg="white", font=("Helvetica", 16)).pack()
    totalAI_lbl = Label(win1, textvariable=totalAI, bg="green", fg="white", font=("Helvetica", 16)).pack()
    reset_btn = Button(win1, text="reset", height=3, width=20, bg="blue", fg="white", command=reset).pack(pady=10)

def newWin2():
    reset()
    win2 = Toplevel(root)
    root.eval(f'tk::PlaceWindow {str(win2)} center') # center screen
    win2.title("Two Player")
    win2.geometry("450x450")
    win2.config(bg="green")
    win2.resizable(False, False)
    roll_btn = Button(win2, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    frame = Frame(win2)
    frame.pack()
    for i in range(0, 6):
        ans = Button(frame, textvariable=dice_rolled[i], height=1, width=2, font=("Helvetica", 20), command=lambda i=i : keep_dice(i)).pack(side=LEFT)
    reset_btn = Button(win2, text="reset", height=3, width=20, bg="blue", fg="white", command=reset).pack(pady=10)
    score_lbl = Label(win2, textvariable=points, bg="green", fg="white", font=("Helvetica", 16)).pack()
    total_lbl = Label(win2, textvariable=total, bg="green", fg="white", font=("Helvetica", 16)).pack()

def newWin3():
    win3 = Toplevel(root)
    reset()
    root.eval(f'tk::PlaceWindow {str(win3)} center') # center screen
    win3.title("Three Player")
    win3.geometry("450x450")
    win3.config(bg="green")
    win3.resizable(False, False)
    roll_btn = Button(win3, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
    frame = Frame(win3)
    frame.pack()
    for i in range(0, 6):
        ans = Button(frame, textvariable=dice_rolled[i], height=1, width=2, font=("Helvetica", 20), command=lambda i=i : keep_dice(i)).pack(side=LEFT)
    reset_btn = Button(win3, text="reset", height=3, width=20, bg="blue", fg="white", command=reset).pack(pady=10)
    score_lbl = Label(win3, textvariable=points, bg="green", fg="white", font=("Helvetica", 16)).pack()
    total_lbl = Label(win3, textvariable=total, bg="green", fg="white", font=("Helvetica", 16)).pack()

def newWin4():
    win4 = Toplevel(root)
    win4.title("How to Play")
    win4.geometry("1200x250")
    win4.config(bg="green")
    title = Label(win4, text="How To Play", bg="green", fg="white", font=("Helvetica", 20)).pack()
    how = Label(win4, text="All players start off with the Scoreboard.\n To get onto the Scoreboard, a player must roll at least 1000 points in a single turn.\nEach turn, players start with 6 dice and roll them all.\n From there, players may choose their scoring dice from any points shown on the board.\n After their choice, they may choose to roll the remaining dice OR keep their points (provided they are on the board or the points are above 1000).\n If a player rolls their dice at their start of their turn and there are no points shown, they may re-roll once.\n On any other occasion, if they roll the dice and there are no points shown, that player will forfeit all points and end their turn.\n When a player has scored and chosen all 6 dice, they MUST keep their points for the turn and reroll all dice.\n To win: A player reaching a score at or above 10,000 becomes the temporary winner, then they must keep their lead as all other players get a chance to roll one more turn.\n The highest score after all players have rolled is the Official Winner", bg="green", fg="white", bd=2, relief="solid", font=("Helvetica", 12)).pack()

# Varaiables with location
title_lbl = Label(root, text="10,000 Dice", fg="white", bg="green", font=("Helvetica", 16)).pack()
player_lbl = Label(root, text="Select the Number of Players", fg="white", bg="green", font=("Helvetica", 16)).pack()
user1_btn = Button(root, text="one", height=3, width=20, bg="blue", fg="white", command=newWin1).pack(pady=10)
user2_btn = Button(root, text="two", height=3, width=20, bg="blue", fg="white", command=newWin2).pack(pady=10)
user3_btn = Button(root, text="three", height=3, width=20, bg="blue", fg="white", command=newWin3).pack(pady=10)
help_btn = Button(root, text="help", height=3, width=20, bg="blue", fg="white", command=newWin4).pack(pady=10)
quit_btn = Button(root, text="quit", height=3, width=20, bg="blue", fg="white", command=on_closing).pack(pady=10)

root.mainloop()
