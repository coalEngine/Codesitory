global_var  = 1
def my_vars():
    print("Global Variable:", global_var)
    local_var = 2
    print('Local Variable', local_var)
    global inner
    inner = 3
    print('Coerced Global:', inner)

my_vars()