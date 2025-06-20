class Vehicle:
    def __init__(self, number):
        self.number = number


class Slot:
    def __init__(self, slot_number):
        self.slot_number = slot_number
        self.vehicle = None

    def park(self, vehicle):
        if not self.vehicle:
            self.vehicle = vehicle
            print(f"Vehicle {vehicle.number} parked at slot {self.slot_number}")
        else:
            print("Slot already occupied")

    def unpark(self):
        if self.vehicle:
            print(f"Vehicle {self.vehicle.number} left slot {self.slot_number}")
            self.vehicle = None
        else:
            print("Slot already empty")


class ParkingLot:
    def __init__(self, size):
        self.slots = [Slot(i) for i in range(1, size + 1)]

    def park_vehicle(self, vehicle):
        for slot in self.slots:
            if not slot.vehicle:
                slot.park(vehicle)
                return
        print("Parking Lot Full")

    def remove_vehicle(self, slot_number):
        if 1 <= slot_number <= len(self.slots):
            self.slots[slot_number - 1].unpark()


lot = ParkingLot(3)
v1 = Vehicle("AP01AB1254")
v2 = Vehicle("AP02CD5279")

lot.park_vehicle(v1)
lot.park_vehicle(v2)
lot.remove_vehicle(1)
lot.park_vehicle(Vehicle("AP03EF9101"))
