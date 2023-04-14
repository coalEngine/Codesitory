import sys
form = []
for _ in range(10):
    nums = ['O']*10
    form.append(nums)
def print_list():
    print(" {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format(form[0][0], form[0][1], form[0][2] , form[0][3] , form[0][4] , form[0][5] , form[0][6] , form[0][7] , form[0][8], form[0][9]))
    print(" {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format(form[1][0], form[1][1], form[1][2] , form[1][3] , form[1][4] , form[1][5] , form[1][6] , form[1][7] , form[1][8], form[1][9]))
    print(" {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format(form[2][0], form[2][1], form[2][2] , form[2][3] , form[2][4] , form[2][5] , form[2][6] , form[2][7] , form[2][8], form[2][9]))
    print(" {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format(form[3][0], form[3][1], form[3][2] , form[3][3] , form[3][4] , form[3][5] , form[3][6] , form[3][7] , form[3][8], form[3][9]))
    print(" {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format(form[4][0], form[4][1], form[4][2] , form[4][3] , form[4][4] , form[4][5] , form[4][6] , form[4][7] , form[4][8], form[4][9]))
    print(" {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format(form[5][0], form[5][1], form[5][2] , form[5][3] , form[5][4] , form[5][5] , form[5][6] , form[5][7] , form[5][8], form[5][9]))
    print(" {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format(form[6][0], form[6][1], form[6][2] , form[6][3] , form[6][4] , form[6][5] , form[6][6] , form[6][7] , form[6][8], form[6][9]))
    print(" {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format(form[7][0], form[7][1], form[7][2] , form[7][3] , form[7][4] , form[7][5] , form[7][6] , form[7][7] , form[7][8], form[7][9]))
    print(" {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format(form[8][0], form[8][1], form[8][2] , form[8][3] , form[8][4] , form[8][5] , form[8][6] , form[8][7] , form[8][8], form[8][9]))
    print(" {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format(form[9][0], form[9][1], form[9][2] , form[9][3] , form[9][4] , form[9][5] , form[9][6] , form[9][7] , form[9][8], form[9][9]))

def change_list(posX, posY):
    form[posX][posY] = 'X'
    print_list()

times = int(input("How many times do you want to change the list?: "))
for _ in range(times):
    selection_1 = int(input("Enter in a row: "))
    selection_2 = int(input("Enter in a column: "))
    change_list(selection_1, selection_2)


