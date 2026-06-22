def greet(temp):
    def mfx(*args, **kwargs):
        print("good morning")
        temp(*args, **kwargs)
        print("thanks for using this function")
    return mfx

@greet
def add(a, b):
    print(a+b)

def hello():
    print("hello")

hello()
add(3, 7)
