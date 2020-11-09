from tkinter import *
from tkinter import messagebox
import random

#Window variables
root = Tk()
root.eval('tk::PlaceWindow . center') # center screen
root.title('10,000 Dice')
root.geometry("400x400")
root.config(bg="green")
root.resizable(False, False) #Disallow players from resizing the window.
stringme=StringVar()
fi=StringVar()
se=StringVar()
th=StringVar()
fo=StringVar()
fit=StringVar()
si=StringVar()
score=IntVar()

# MessageBox on Close
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
    dice_count = [0] * 6
    for i in range(0, 6):
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
    
    lis = " ".join(map(str,ls)) # list to string
    fi.set(ls[0])
    se.set(ls[1])
    th.set(ls[2])
    fo.set(ls[3])
    fit.set(ls[4])
    si.set(ls[5])
    stringme.set(lis)
    new_score = temp_score
    score.set(new_score)

def deleteme():
    fi.set("\u2680")
    se.set("\u2680")
    th.set("\u2680")
    fo.set("\u2680")
    fit.set("\u2680")
    si.set("\u2680")


# reset dice 
def forget():
    stringme.set("")
    if score.get() > 0: # only pop if you press reset
        messagebox.showinfo("info", "No Points left, End of turn")
    score.set(0)

def newWin1():
    forget()
    win1 = Toplevel(root)
    root.eval(f'tk::PlaceWindow {str(win1)} center') # center screen
    win1.title("One Player")
    win1.geometry("400x400")
    win1.config(bg="green")
    # win1.resizable(False, False)
    user41_btn = Button(win1, text="roll", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(side=TOP)
    #result_lblse = Label(win1, textvariable=stringme, bg="green", fg="black", font=("Helvetica", 30)).pack(side=TOP,fill=BOTH)
    #a = Label(win1, text="", bg="green").pack(side=LEFT,padx=30)
    r1 = Button(win1, textvariable=fi, height=0, width=0, bg="grey", fg="white", font=("Helvetica", 20), command=deleteme).pack(side=LEFT)
    r2 = Button(win1, textvariable=se, height=0, width=0, bg="grey", fg="white", font=("Helvetica", 20), command=deleteme).pack(side=LEFT)
    r3 = Button(win1, textvariable=th, height=0, width=0, bg="grey", fg="white", font=("Helvetica", 20), command=deleteme).pack(side=LEFT)
    r4 = Button(win1, textvariable=fo, height=0, width=0, bg="grey", fg="white", font=("Helvetica", 20), command=deleteme).pack(side=LEFT)
    r5 = Button(win1, textvariable=fit, height=0, width=0, bg="grey", fg="white", font=("Helvetica", 20), command=deleteme).pack(side=LEFT)
    r6 = Button(win1, textvariable=si, height=0, width=0, bg="grey", fg="white", font=("Helvetica", 20), command=deleteme).pack(side=LEFT) #side=LEFT, fill=NONE, expand=False
    a = Label(win1, text="", bg="green").pack(side=LEFT,padx=30)
    user41_btn = Button(win1, text="delete dice", height=3, width=20, bg="blue", fg="white", command= forget).pack(side=BOTTOM)
    score_lbl = Label(win1, textvariable=score, bg="green", fg="black", font=("Helvetica", 16)).pack(side=BOTTOM)


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
quit_btn = Button(root, text="quit", height=3, width=20, bg="blue", fg="white", command=on_closing).pack(pady=10)
# user4_btn = Button(root, text="change me", height=3, width=20, bg="blue", fg="white", command=randomGen).pack(pady=10)
# result_lbls = Label(root, textvariable=stringme, bg="black", fg="white", font=("Helvetica", 30)).pack()

root.mainloop()