class employee:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        
    def show_details(self):
        print(f"the employee name {self.id} is {self.name}")
            
class programmers(employee):
    def show_language(self):
        print("the default language is python")    
        
e1 = employee(1, "raju")
e1.show_details()       
e2 = programmers(2, "nitin")
e2.show_details()
e2ffffff.show_language() 