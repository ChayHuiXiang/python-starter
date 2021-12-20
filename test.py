class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return print('The {self.color} car has {self.mileage} miles.')
Car(color="blue",mileage=20000)
Car(color="red",mileage=30000)