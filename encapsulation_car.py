class Car:
    def __init__(self, petrol: int=0, odometer: int=0):
        if petrol <= 60:
            self.__petrol = petrol
        else:
            self.__petrol = 60
        self.__odometer = odometer

    def fill_up(self):
        if self.__petrol < 60:
            self.__petrol = 60
        else:
            pass

    def drive(self, km: int):
        if km <= self.__petrol and km > 0:
            self.__odometer += km
            self.__petrol -= km
        elif km > self.__petrol and km > 0:
            self.__odometer += self.__petrol
            self.__petrol = 0


    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining: {self.__petrol} litres"

if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)