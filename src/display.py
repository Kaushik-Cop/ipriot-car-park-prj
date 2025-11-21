class Display:
    def __init__(self, id, message="", is_on=False):
        self.id = id
        self.message = message
        self.is_on = is_on

    def update(self, carpark):

        spaces_left = carpark.capacity - len(carpark.plates)
        if spaces_left > 0:
            self.message = f"{spaces_left} spaces available"
        else:
            self.message = "Car park FULL"
        self.is_on = True

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")
    def __str__(self):
        return f"Display {self.id}: {self.message}"


pass
