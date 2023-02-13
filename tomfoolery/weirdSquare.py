button_dict = {}
for x in range(7):
    for y in range(6):
   #
   # def action(x = x): 
   #    return text_updation(x)   
   # create the buttons 
      
        pos_x += 1
        pos_y += 1
        button_dict[x] = Button(window, text = x, width=5, height=2, bg="black")
        button_dict[x].place(x=150+pos_x, y=120+pos_y)
