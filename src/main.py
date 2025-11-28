from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display



car_park = CarPark("moondalup", 100, log_file="moondalup.txt")

car_park.write_config("moondalup_config.json")


car_park = CarPark.from_config("moondalup_config.json")


entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)


exit_sensor = ExitSensor(id=2, is_active=True, car_park=car_park)


display = Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=car_park)


for i in range(10):
    entry_sensor.detect_vehicle()



cars_to_exit = list(car_park.plates)[:2]
for plate in cars_to_exit:
    exit_sensor.detect_vehicle(plate)

#test program
print(f"\nCars in car park: {car_park.capacity - car_park.available_bays}")
print(f"Available bays: {car_park.available_bays}")