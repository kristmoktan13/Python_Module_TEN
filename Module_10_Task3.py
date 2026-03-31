class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")
    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")
    def go_to_floor(self, target_floor):
        print(f"\nMoving from floor {self.current_floor} to floor {target_floor}")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {self.current_floor}")
class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(num_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)
            print(f"Elevator {i + 1} created")
    def run_elevator(self, elevator_number, destination_floor):
        index = elevator_number - 1
        if 0 <= index < len(self.elevators):
            print(f"\n Running Elevator {elevator_number} ")
            self.elevators[index].go_to_floor(destination_floor)
        else:
            print(f"Error: Elevator {elevator_number} does not exist")
    def fire_alarm(self):
        print("\n FIRE ALARM ACTIVATED")
        print("Moving all elevators to bottom floor...\n")
        for i, elevator in enumerate(self.elevators, 1):
            print(f"Elevator {i}:")
            elevator.go_to_floor(self.bottom_floor)
        print("\n All elevators at bottom floor. Building evacuated.")
building = Building(1, 10, 3)
building.run_elevator(1, 7)
building.run_elevator(2, 5)
building.run_elevator(3, 9)
building.fire_alarm()