import unittest
from src.car_park import CarPark
from src.sensor import EntrySensor, ExitSensor

class TestSensors(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry = EntrySensor(1, car_park=self.car_park)
        self.exit = ExitSensor(2, car_park=self.car_park)

    def test_entry_sensor_adds_car(self):
        self.entry.update_car_park("TEST-001")
        self.assertIn("TEST-001", self.car_park.plates)
        self.assertEqual(self.car_park.available_bays, 99)

    def test_exit_sensor_removes_car(self):
        self.car_park.add_car("TEST-001")
        self.exit.update_car_park("TEST-001")
        self.assertNotIn("TEST-001", self.car_park.plates)
        self.assertEqual(self.car_park.available_bays, 100)

if __name__ == "__main__":
    unittest.main()
