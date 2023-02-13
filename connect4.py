
move_player = 'O'
move_player_2 = "\033[1;33;47m O"

square_obj = {

    "square_piece_1": " _____",
    "square_piece_2": "|     |",
    "square_piece_3": "|_____|",
}




val = 0

def draw_square():
    print(square_obj["square_piece_1"])
    print("|     |")
    print(square_obj["square_piece_3"])

for _ in range(10):
    print()
print("Connect 4!")
print()

for _ in range(6):
    for _ in range(7):
        draw_square()
   
    
print("       ")

            
       