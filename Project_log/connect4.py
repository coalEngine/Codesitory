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

# Settings
game_over = False

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

COORDS_LIST = []
buttons_dict = {}

###########################################
def fire_off(x, y):
    print("column:{}, row:{}".format(x, y))
    newValue = 0
    value = '{}_{}'.format(x, y)

###########################################

for r in range(6):
    for c in range(7):
        coord = str(r)+"_"+str(c)
        COORDS_LIST.append(coord)
        buttons_dict[COORDS_LIST[-1]] = Button(frame, text="O", width="16", height="7", bg="Black", fg="White")
        ###########################################################################
        buttons_dict[COORDS_LIST[-1]]["command"] = lambda x=c, y=r : fire_off(x, y)
        ###########################################################################
        buttons_dict[COORDS_LIST[-1]].grid(row=r,column=c)

print(COORDS_LIST)
        
def run():
    main_text.place(x=536, y=0)
    player_select.place(x=0, y=0)
    window.mainloop()


while not game_over:
    run()

            
       