def sum(x):

    if x==0:
        return 0
    else:
        s = x + sum(x - 1)
        return s

def fact(x):
    if x==0:
        return 1
    else:
        f = x *fact(x-1)
        return f
print(sum(5))

print(fact(5))