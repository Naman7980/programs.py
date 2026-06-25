class person:
    def __init__(self, name, age):
        self.name = name
        self.age = 21
        
a = person("pankaj", 21)  
print(a.__dict__)      
    
print(help(person))    