class Car:
    def __init__(self,year,make,model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return 2019-self.year
        
myCar = Car(1996,'cool','ftw')
print(myCar.age())