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
    turnVar.set("AI's turn")
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
            turnVar.set("Player's turn")
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
    turnVar.set("Player's turn")
    turn_lbl = Label(win1, textvariable=turnVar, bg="green", fg="white", font=("Helvetica", 16)).pack()
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
    rollon_btn = Button(frame2, text="Keep points and \nRoll the remaining dice", height=3, width=20, bg="blue", fg="white", command=reroll).pack(side=LEFT, padx=10, pady=10)
    endturn_btn = Button(frame2, text="End Turn and \nAdd Points to Score", height=3, width=20, bg="blue", fg="white", command=endTurn).pack(padx=10, side=LEFT, pady=10)

    #SCOREBOARD
    frame3 = Frame(win1, bg="green")
    frame3.pack()
    player_lbl = Label(win1, text="Player's points", bg="green", fg="white", font=("Helvetica", 16)).pack()
    score_lbl = Label(win1, textvariable=points, bg="green", fg="white", font=("Helvetica", 16)).pack()
    player2_lbl = Label(win1, text="Player's total", bg="green", fg="white", font=("Helvetica", 16)).pack()
    total_lbl = Label(win1, textvariable=total, bg="green", fg="white", font=("Helvetica", 16)).pack()
    AI_lbl = Label(win1, text="AI's points", bg="green", fg="white", font=("Helvetica", 16)).pack()
    scoreAI_lbl = Label(win1, textvariable=pointsAI, bg="green", fg="white", font=("Helvetica", 16)).pack()
    AI2_lbl = Label(win1, text="AI's total", bg="green", fg="white", font=("Helvetica", 16)).pack()
    totalAI_lbl = Label(win1, textvariable=totalAI, bg="green", fg="white", font=("Helvetica", 16)).pack()
    reset_btn = Button(win1, text="reset", height=3, width=20, bg="blue", fg="white", command=reset).pack(pady=10)

def how_to_play():
    winHelp = Toplevel(root)
    winHelp.title("How to Play")
    winHelp.geometry("1200x250")
    winHelp.config(bg="green")
    title = Label(winHelp, text="How To Play", bg="green", fg="white", font=("Helvetica", 20)).pack()
    how = Label(winHelp, text="All players start off with the Scoreboard.\n To get onto the Scoreboard, a player must roll at least 1000 points in a single turn.\nEach turn, players start with 6 dice and roll them all.\n From there, players may choose their scoring dice from any points shown on the board.\n After their choice, they may choose to roll the remaining dice OR keep their points (provided they are on the board or the points are above 1000).\n If a player rolls their dice at their start of their turn and there are no points shown, they may re-roll once.\n On any other occasion, if they roll the dice and there are no points shown, that player will forfeit all points and end their turn.\n When a player has scored and chosen all 6 dice, they MUST keep their points for the turn and reroll all dice.\n To win: A player reaching a score at or above 10,000 becomes the temporary winner, then they must keep their lead as all other players get a chance to roll one more turn.\n The highest score after all players have rolled is the Official Winner", bg="green", fg="white", bd=2, relief="solid", font=("Helvetica", 12)).pack()

# Varaiables with location
title_lbl = Label(root, text="10,000 Dice", fg="white", bg="green", font=("Helvetica", 16)).pack()
play_btn = Button(root, text="Play", height=3, width=20, bg="blue", fg="white", command=newWin1).pack(pady=10)
help_btn = Button(root, text="Help", height=3, width=20, bg="blue", fg="white", command=how_to_play).pack(pady=10)
quit_btn = Button(root, text="Quit", height=3, width=20, bg="blue", fg="white", command=on_closing).pack(pady=10)

root.mainloop()
