def fun(x):
    return x>5

l=[3,4,2,1,3,4,78,87]

newl = list(filter(fun, l))
print(newl)