from tkinter import *
import random

root=Tk()
root.title("Roll Dice")
root.geometry("500x400")

label=Label(root,font=('helvetica',250,'bold'),text="")

def roll_dice():
    dice_number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice_number)}')
    label.pack()


button=Button(root,font=('helvetica',25,'bold'),text="Roll Dice",command=roll_dice)
button.pack()
root.mainloop()


