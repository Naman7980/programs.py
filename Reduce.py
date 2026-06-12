from functools import reduce
l = [2,4,5,6,2,1,9]

def sum(x,y):
    return x+y

newl = reduce(sum, l)
print(newl)