from tkinter import *

root = Tk()
root.title('CAPSTONE Project')
root.geometry("400x400")

# Varaiables
user1_lbl = Button(root, text="one users", height=3, width=20, bg="green")
user2_lbl = Button(root, text="two users", height=3, width=20, bg="blue")

# Location
user1_lbl.place(x=200, y=150, anchor="center")
user2_lbl.place(x=200, y=250, anchor="center")

root.mainloop()