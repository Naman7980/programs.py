class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = 12000
    @classmethod    
    def splitfromstr(danger, string):
        return danger(string.split("-")[0], string.split("-")[1])     
        
a1 = employee("Harry", 12000)
print(a1.name)
print(a1.salary)

string = "Naman-12000"
a2 = employee.splitfromstr(string)
print(a2.name)
print(a2.salary)

        
        