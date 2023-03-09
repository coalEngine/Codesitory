from tkinter import *
import tkinter as tk

# Window Config
window = Tk()
window.title("Connect 4 (v1.0)")
window.geometry("1200x800")
window.config(bg="black")

# Frame Config
frame = Frame(window, bg="White")
frame.grid(column=0,row=0)
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
catch_player = Label(
    fg="White",
    bg="Black",
    text=""
)

def drop_down():
    pass

# create buttons

COORDS_LIST = []
buttons_dict = {}


###########################################
def select_move(x, y):
    print("column:{}, row:{}".format(x, y))
    value = '{}_{}'.format(y, x)
    COORDS_LIST.sort()
    if value in COORDS_LIST:
        if player_select.cget("text") == "Player_1_Turn":
            if buttons_dict[value].cget("fg") == "Red":
                catch_player.config(text="(P1): You cannot move here")
            elif buttons_dict[value].cget("fg") == "Blue":
                catch_player.config(text="(P1): You've already moved here")
            else:
                buttons_dict[value].config(text="O", fg="Blue")
                player_select.config(text="Player_2_Turn")
                catch_player.config(text="")
        elif player_select.cget("text") == "Player_2_Turn":
            if buttons_dict[value].cget("fg") ==  "Blue":
                catch_player.config(text="(P2): You cannot move here")
            elif buttons_dict[value].cget("fg") == "Red":
                catch_player.config(text="(P2): You've already moved here")
            else:
                buttons_dict[value].config(text="O", fg="Red")
                player_select.config(text="Player_1_Turn")
                catch_player.config(text="")
###########################################

for r in range(6):
    for c in range(7):
        coord = str(r)+"_"+str(c)
        COORDS_LIST.append(coord)
        buttons_dict[COORDS_LIST[-1]] = Button(frame, text="O", width="16", height="7", bg="Black", fg="White")
        ###########################################################################
        buttons_dict[COORDS_LIST[-1]]["command"] = lambda x=c, y=r : select_move(x, y)
        ###########################################################################
        buttons_dict[COORDS_LIST[-1]].grid(row=r,column=c)


def run():
    main_text.place(x=536, y=0)
    player_select.place(x=0, y=0)
    catch_player.place(x=0, y=20)
    window.mainloop()


while not game_over:
    run()

            
       