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
        if self.available_bays > 0:
            self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        if plate not in self.plates:
            raise ValueError(f"Car {plate} is not found")
        self.plates.remove(plate)

        self.update_displays()

    def update_displays(self):
        for display in self.displays:
            display.update(self)

    @property
    def available_bays(self):
        return max(self.capacity - len(self.plates), 0)


    def update_display(self, display):
        data ={"available_bays": self.available_bays, "temperature": 25}

        for display in self.displays:
            display.update(data)
    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."


pass
