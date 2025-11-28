class Display:
    def __init__(self, id, message="", is_on=False, car_park=None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def update(self, carpark):

        spaces_left = carpark.available_bays
        if spaces_left > 0:
            self.message = f"{spaces_left} spaces available"
        else:
            self.message = "Car park FULL"
        self.is_on = True

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
    def __str__(self):
        return f"Display {self.id}: {self.message}"


pass
