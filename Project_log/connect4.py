from tkinter import *
import tkinter as tk

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
board = [
    [],
    [],
    [],
    [],
    [],
    []
]

# Main Text Config
main_text = Label(
    text="Connect 4",
    font = ('Times 24 italic'),
    bg="Black",
    fg="White"
    )

def drop_down():
    pass

# create buttons
button_dict = {}
for y_pos in range(7):
    for x_pos in range(6):
   #
   # def action(x = x): 
   #    return text_updation(x)   
   # create the buttons 
        button_dict[y_pos] = Button(
            frame, 
            text = '', 
            width=16, 
            height=7, 
            bg="Black",
         
        )
        button_dict[y_pos].grid(row=x_pos, column=y_pos)
        
        
def run():
    main_text.pack()
    window.mainloop()
    
    
run()

            
       