from time import *
start_timer = time()
struct = localtime(start_timer)
print("\nStarting countdown at:", strftime('%X', struct))

i = 10
while i > -1:
    print(i)
    i -= 1
    sleep(1)

end_time = time()
diff = round(end_time - start_timer)
print("Runtime", diff, 'secs')