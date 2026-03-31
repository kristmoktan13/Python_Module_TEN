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
h = Elevator(1, 10)
h.go_to_floor(5)
h.go_to_floor(1)