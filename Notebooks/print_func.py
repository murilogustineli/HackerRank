import random

n = random.randint(20, 30)
lst = []

def print_func(x):
    for i in range(1, x+1):
        lst.append(i)

print_func(n)
print(*lst, sep=', ')
