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

selected = "Player_1_Turn"

player_select = Label(
    fg="White",
    bg="Black",
    text= selected
)

def drop_down():
    pass



  

# create buttons

button_dict = {}

for y_pos in range(7):
    for x_pos in range(6):
        def change_player():
            player_select.config(text="Player_2_Turn")
            p2 = True
        
     # create the buttons 
        button_dict[y_pos] = Button(
            frame, 
            text = '', 
            width=16, 
            height=7, 
            bg="Black",
            command = change_player,
            fg="Light Blue",
        )
        button_dict[y_pos].grid(row=x_pos, column=y_pos)
        
        
def run():
    main_text.pack()
    player_select.place(x=0, y=0)
    window.mainloop()

def create_virtual_board():
    board = np.zeros((6,7))
    return board

board_data = [
                [frame.children["!button"], frame.children["!button2"], frame.children["!button3"], frame.children["!button4"], frame.children["!button5"], frame.children["!button6"], frame.children["!button7"]],
                [frame.children["!button8"], frame.children["!button9"], frame.children["!button10"], frame.children["!button11"], frame.children["!button12"], frame.children["!button13"], frame.children["!button14"]],
                [frame.children["!button15"], frame.children["!button16"], frame.children["!button17"], frame.children["!button18"], frame.children["!button19"], frame.children["!button20"], frame.children["!button21"]],
                [frame.children["!button22"], frame.children["!button23"], frame.children["!button24"], frame.children["!button25"], frame.children["!button26"], frame.children["!button27"], frame.children["!button28"]],
                [frame.children["!button29"], frame.children["!button30"], frame.children["!button31"], frame.children["!button32"], frame.children["!button33"], frame.children["!button34"], frame.children["!button35"]],
                [frame.children["!button36"], frame.children["!button37"], frame.children["!button38"], frame.children["!button39"], frame.children["!button40"], frame.children["!button41"], frame.children["!button42"]]
            ]
board = create_virtual_board()
print(board)    

while not game_over:
    run()

            
       