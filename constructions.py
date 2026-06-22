class person:
    
    def __init__(self, name, occ):
        print("Hey i am a person")
        self.name = name
        self.occ = occ

    def info(self):
     print(f"{self.name} is a {self.occ}")

a = person("Maman", "Software developer")    
b = person("Nanan", "manager")

a.info()
b.info()