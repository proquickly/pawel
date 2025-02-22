class Car:
    def __init__(self, color):
        self.color = color

    def sound_horn(self):
        print("beep")


# instantiation
mycar = Car("red")
mycar.sound_horn()
print(mycar.color)

myother_car = Car("blue")
myother_car.sound_horn()
print(myother_car.color)
