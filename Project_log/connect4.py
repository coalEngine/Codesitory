from tkinter import *
import tkinter as tk
import numpy as np

# Window Config
window = Tk()
window.title("Connect 4 (v1.0)")
window.geometry("1200x800")
window.config(bg="black")

# Frame Config
frame = Frame(window, bg="White")
frame.pack(side=BOTTOM)

# Game_Board Config
player_1_token = ""
player_2_token = ""
e = " "

# Settings
game_over = False
turn = 0
text="player_1_turn"


# Main Text Config
main_text = Label(
    text="Connect 4",
    font = ('Times 24 italic'),
    bg="Black",
    fg="White"
    )

def drop_down():
    pass

text = Entry(window, width=30, bg='Black', fg="White")
text.place(x=0, y=0)

def text_updation():
     text.delete(0, END)
     if turn == 0: 
        text.insert(0, "player_1_turn")
     
  


# create buttons
button_dict = {}
for y_pos in range(7):
    for x_pos in range(6):
   
        def action(): 
            return text_updation()  
      
     # create the buttons 
        button_dict[y_pos] = Button(
            frame, 
            text = '', 
            width=16, 
            height=7, 
            bg="Black",
            command= action
        )
        button_dict[y_pos].grid(row=x_pos, column=y_pos)
        
        
def run():
    main_text.pack()
    window.mainloop()

def create_virtual_board():
    board = np.zeros((6,7))
    return board


board = create_virtual_board()
print(board)    

while not game_over:
    run()

            
       