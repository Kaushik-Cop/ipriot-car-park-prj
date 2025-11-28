from abc import ABC, abstractmethod
import random
class Sensor:
    def __init__(self, id, is_active=False, car_park=None):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        status = "active" if self.is_active else "inactive"
        return f"Sensor {self.id} is {status}."

    def update_car_park(self, plate):
      pass

    def scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self, plate=None):
        if plate is None:
            plate = self.scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")
    pass


class ExitSensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        if self.car_park.plates:
            return random.choice(self.car_park.plates)
        return None
    pass
