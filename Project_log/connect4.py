from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Connect 4!")


# create buttons
button_dict = {}
for x in range(7):
    for y in range(6):
   #
   # def action(x = x): 
   #    return text_updation(x)   
   # create the buttons 
        button_dict[x] = Button(window, text = '', width=5, height=2, bg="white")
        button_dict[x].place(x=150*x, y=120*y)

        
d = 10
def run():
    window.mainloop()

run()

            
       