from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Connect 4!")

def switchPlayers():
    pass


for y in range(7):
    for x in range(6):
            new = tk.Button(
            fg="white",
            bg="black",
            width=5,
            height=2
            )
            new.place(x=150*x, y=120*y)

print("       ")
window.mainloop()
            
       