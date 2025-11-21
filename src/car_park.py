from sensor import Sensor
from display import Display
class CarPark:
    def __init__(self, location="Unknown", capacity=0, plates=None, displays=None):
        self.location = location
        self.capacity = capacity

        self.plates = plates or []
        self.displays = displays or []

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)

        if isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
        self.update_displays()

    def update_displays(self):
        for display in self.displays:
            display.update(self)

    def available_bays(self):
        bays = self.capacity - len(self.plates)
        if bays < 0:
            bays = 0
        return bays

    def update_display(self, display):
        data ={"available_bays": self.available_bays, "temperature": 25}

        for display in self.displays:
            display.update(data)
    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."


pass
