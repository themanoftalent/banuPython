# You can use break in Python in all the loops: while, for, and nested. If you are using it in nested loops, 
# it will terminate the innermost loop where you have used it, and the control of the program will flow to the outer loop.


def find_age(name, ages):
    for n, a in ages:
       if n == name:
           break
    else:
        raise ValueError('Name not found')
    return a

ages = [('Alice', 32), ('Bob', 48), ('Charlie', 28)]
print(find_age('Bob', ages))
