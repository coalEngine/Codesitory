import sys
form = []
for _ in range(10):
    nums = ['O']*10
    form.append(nums)
def print_list():
    print("[{},".format(form[0]))
    print(" {},".format(form[1]))
    print(" {},".format(form[2]))
    print(" {},".format(form[3]))
    print(" {},".format(form[4]))
    print(" {},".format(form[5]))
    print(" {},".format(form[6]))
    print(" {},".format(form[7]))
    print(" {},".format(form[8]))
    print(" {}]".format(form[9]))

def change_list(posX, posY):
    form[posX][posY] = 'X'
    print_list()

times = int(input("How many times do you want to change the list?: "))
for _ in range(times):
    selection_1 = int(input("Enter in a row: "))
    selection_2 = int(input("Enter in a column: "))
    change_list(selection_1, selection_2)


