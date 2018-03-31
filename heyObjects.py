class Animal:
    species ="cat"
    moniker = "Shiva"
    age = "5"
    
    def toString(self):
        print(self.moniker + " is a " + self.age + "-year-old " + self.species)
        
myPet = Animal()
myPet.toString()

    