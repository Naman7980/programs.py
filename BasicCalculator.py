

a = float(input("enter first digits\n"))


b = float(input("enter second digits\n"))


c = input("choose any following method: '+','-','*','/'\n")


match c:
    case '+':

        print("this is your solution: ",a+b)

    case '-':

        print("this is your solution: ",a-b)
    
    case '*':

        print("this is your solution: ",a*b)

    case '/':

        print("this is your solution: ",a/b)



