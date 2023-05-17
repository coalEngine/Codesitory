
import numpy as np
import matplotlib.pyplot as plt

key1_name = input("Item?: ")
val1 = int(input("Value?: "))
key2_name = input("Item?: ")
val2 = int(input("Value?: "))
key3_name = input("Item?: ")
val3 = int(input("Value?: "))
key4_name = input("Item?: ")
val4 = int(input("Value?: "))
key5_name = input("Item?: ")
val5 = int(input("Value?: "))

title = input("Please title the graph: ")
 
  
# creating the dataset
data = {key1_name:val1, key2_name:val2, key3_name:val3,
        key4_name:val4, key5_name:val5}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='maroon',
        width = 0.4)
 

plt.title(title)
plt.show()