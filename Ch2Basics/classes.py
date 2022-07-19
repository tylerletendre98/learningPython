
class Vehilce():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle
    def drive(self, speed):
        self.mode = 'driving'
        self.speed = speed

class Car(Vehilce):
    def __init__(self, enginetype):
        super().__init__('Car')
        self.wheels = 4 
        self.doors= 4 
        self.enginetype = enginetype
    def drive(self, speed):
        super().drive(speed)
        print ('Driving my', self.enginetype, 'car at', self.speed)

class Motorcycle(Vehilce):
    def __init__(self, enginetype, hassidecar):
        super().__init__('Motorcycle')
        if (hassidecar):
            self.wheels= 3
        else:
            self.wheels = 2
        self.doors= 0
        self.enginetype = enginetype
    def drive(self, speed):
        super().drive(speed)
        print ('Driving my', self.enginetype, 'motorcycle at', self.speed)
        
car1 = Car('gas')
car2 = Car('electric')
car3 = Car('diesel')
mc1 = Motorcycle('gas', False)

# print(car1.enginetype)
# print(car2.doors)
# print(car3.wheels)
# print(mc1.wheels)


car1.drive(50)
car2.drive(40)
mc1.drive(60)