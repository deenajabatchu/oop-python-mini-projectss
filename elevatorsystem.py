class Elevator:
    def __init__(self, max_floor):
        self.current_floor = 0
        self.max_floor = max_floor

    def move_to(self, floor):
        if floor>=0 and floor <= self.max_floor:
            print(f"Moving from floor {self.current_floor} to floor {floor}")
            self.current_floor = floor
        else:
            print("Invalid floor")

    def status(self):
        print(f"Elevator is at floor {self.current_floor}")


elevator = Elevator(10)
elevator.status()
elevator.move_to(5)
elevator.move_to(11)
elevator.move_to(0)
