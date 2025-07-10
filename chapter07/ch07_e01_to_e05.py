print("Exercise-7.1")
def print_x(x):
    print(int(x)+5)
def main():
    print_x('25')
main()
print("-"*10)

print("Exercise-7.2")
def print_me(x):
    print(x+2)
def print_me(x):
    print(x+3)
print_me(5)
print("-"*10)

print("Exercise-7.3")
def make_total(type, *args):
    """
    This function can take multiple arguments.
    However, it considers only the integers, floating-point numbers
    and string data types.
    """
    if type=='strings':
        total=''
    elif type == 'numbers':
        total = 0.0
    # Traversing the arguments
    for item in args:
        total= total + item
    return total

result = make_total("numbers",2.5,3)
print(result)
result = make_total("strings","2.75","3")
print(result)
print("-"*10)

print("Exercise-7.4")
x = 10
print(f"x = {x}")

# def print_me():
def print_me(x):
    x += 2
    print(f"Now x is: {x}")

print_me(x)
print(f"Here x is: {x}")

print("-"*10)
print("Exercise-7.5")
def print_me(x):
    print(x)

def print_me(x,y):
    print(x+y)

print_me(5) # will raise error now
print_me(5,7)
print("-"*10)


