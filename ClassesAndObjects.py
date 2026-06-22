class person:
    name = "naman"
    occupation = "software developer"

    def info(self):
     print(f"{self.name} is a {self.occupation}")

a = person()    
a.name = "Manan"
a.occupation = " tutor"
a.info()
