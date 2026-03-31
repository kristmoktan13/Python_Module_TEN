import random
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
        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
        self.hours_passed = 0
    def hour_passes(self):
        self.hours_passed += 1
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
    def print_status(self):
        for i in range(len(self.cars)):
            for j in range(len(self.cars) - 1):
                if self.cars[j].travelled_distance < self.cars[j + 1].travelled_distance:
                    temp = self.cars[j]
                    self.cars[j] = self.cars[j + 1]
                    self.cars[j + 1] = temp
        print("=" * 70)
        print(f"Race: {self.name}   |   Hour: {self.hours_passed}")
        print("=" * 70)
        print(f"{'Rank':<6} {'Registration':<15} {'Max Speed':<12} {'Current Speed':<15} {'Distance (km)':<15}")
        print("-" * 70)
        for rank in range(len(self.cars)):
            car = self.cars[rank]
            finished = " FINISHED" if car.travelled_distance >= self.distance else ""
            print(f"{rank + 1:<6} {car.registration_number:<15} {car.max_speed:<12} {car.current_speed:<15} {car.travelled_distance:<15.1f}{finished}")
        print("=" * 70)
    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False
cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    car = Car(reg_number, max_speed)
    cars.append(car)
race = Race("Grand Demolition Derby", 8000, cars)
while not race.race_finished():
    race.hour_passes()
    if race.hours_passed % 10 == 0:
        race.print_status()
if race.hours_passed % 10 != 0:
    race.print_status()
print(f"\nRace finished after {race.hours_passed} hours!")
for car in race.cars:
    if car.travelled_distance >= race.distance:
        print(f"  Winner: {car.registration_number} with {car.travelled_distance:.1f} km!")
