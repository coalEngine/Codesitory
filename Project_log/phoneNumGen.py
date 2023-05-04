import random
def generateNumber():
    set1 = []
    set2 = []
    set3 = []
    for _ in range(3):
        piece = int(round(random.random() * 7, 0))
        if piece == 0 and _ == 0:
            piece = int(round(random.random() * 7, 0))
        set1.append(piece)
    for _ in range(3):
        piece = int(round(random.random() * 9, 0))
        if piece == 0 and _ == 0:
            piece = int(round(random.random() * 9, 0))
        set2.append(piece)
    for _ in range(4):
        piece = int(round(random.random() * 9, 0))
        set3.append(piece)
    whole_piece_1 = int(str(set1[0]) + str(set1[1]) + str(set1[2]))
    whole_piece_2 = int(str(set2[0]) + str(set2[1]) + str(set2[2]))
    whole_piece_3 = int(str(set3[0]) + str(set3[1]) + str(set3[2]) + str(set3[3]))
    while whole_piece_2 > 742:
        whole_piece_2 -= 1
    print(f"\n\nGenerated Number:\n{whole_piece_1}-{whole_piece_2}-{whole_piece_3}\n\n\n")

generateNumber()