class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f"{self.name}: The car went!")

    def stop(self):
        print(f"{self.name}: The car stopped")

    def turn(self, direction):
        print(f"{self.name}: the car turned {'left' if direction == 0 else 'right'}.")

    def show_speed(self):
        return f"{self.name}: The car has speed: {self.speed}"


class TownCar(Car):
    def show_speed(self):
        return (f"{self.name}: The car has speed: {self.speed}. Over speed!"
                    if self.speed > 60 else f"{self.name}: The car has speed: {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        return (f"{self.name}: The car has speed: {self.speed}. Over speed!"
                    if self.speed > 40 else f"{self.name}: The car has speed: {self.speed}")


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police=True):
        super().__init__(name, speed, color, is_police)


towncar = TownCar("Opel", 80, "blue")
towncar.go()
towncar.turn(0)
print(towncar.show_speed())
towncar.stop()
print()

workcar = WorkCar("Nissan", 35, "black")
workcar.go()
workcar.turn(1)
print(workcar.show_speed())
workcar.stop()
print()

sportcar = SportCar("Bugatti", 240, "red")
sportcar.go()
sportcar.turn(1)
print(sportcar.show_speed())
sportcar.turn(0)
sportcar.stop()
print()

policecar = PoliceCar("BMW", 120, "blue")
policecar.go()
policecar.turn(1)
print(policecar.show_speed())
policecar.stop()
print()

print(f"The car {sportcar.name} (color: {sportcar.color})")
print(f"The car {towncar.name} (speed: {towncar.speed})")
