class PartyAnimal:
    x=0
    def __init__(self):
        print(self,"created.")
    def party(self):
        self.x=self.x+1
        print(self,"has x value of",self.x)
    def __del__(self):
        print(self,"destroyed.")

a=PartyAnimal()
a.party()
a.party()