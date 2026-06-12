def apply(a,value):
    return 3 + a(value)

cube = lambda x: x*x*x

print(cube(lambda x: x*x*x, 2))    
