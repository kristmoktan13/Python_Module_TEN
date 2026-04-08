class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_kwh):
        super().__init__(registration_number, max_speed)
        self.battery_kwh = battery_kwh
class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_liters):
        super().__init__(registration_number, max_speed)
        self.tank_liters = tank_liters
electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)
electric.accelerate(150)
gasoline.accelerate(120)
electric.drive(3)
gasoline.drive(3)
print(f"Electric car ({electric.registration_number}) km counter: {electric.travelled_distance} km")
print(f"Gasoline car ({gasoline.registration_number}) km counter: {gasoline.travelled_distance} km")