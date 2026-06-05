pricemoney = 0
print("<Welcome to kaun banega crorepati>")

print("your first question is:")
a = input("kya aapke toothpast me namak hai?: ")
if a == 'yes':
    print("correct answer")
    pricemoney += 10000000
else:
    print("wrong answer hahaha! you are going to the next question")    


print("your second question is:")
b = input("1 derzon bananas me kitne banana hote hai?: ")
if (int(b) == 12):
    print("correct answer")
    pricemoney += 10000000
else:
    print("wrong answer hahaha! you are going to the next question")   

print("your third question is:")
c = input("1 kg me kitne gm hote hai?: ")   
if int(c) == 1000:
    print("correct answer")
    pricemoney += 10000000
else:
    print("wrong answer hahaha!")  

print("here is your total winning price money: ", pricemoney)       



    



