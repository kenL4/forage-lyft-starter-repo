import unittest
from datetime import datetime

from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine

from battery import spindler_battery
from battery import nubbin_battery

from tire import carrigan_tire
from tire import octoprime_tire

class TestCapuletEngine(unittest.TestCase):
    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        test_engine = capulet_engine.CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertTrue(test_engine.needs_service())

    def test_capulet_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        test_engine = capulet_engine.CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertFalse(test_engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_sternman_engine_should_be_serviced(self):
        warning_light_on = True

        test_engine = sternman_engine.SternmanEngine(warning_light_on=warning_light_on)
        self.assertTrue(test_engine.needs_service())

    def test_sternman_engine_should_not_be_serviced(self):
        warning_light_on = False

        test_engine = sternman_engine.SternmanEngine(warning_light_on=warning_light_on)
        self.assertFalse(test_engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        test_engine = willoughby_engine.WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertTrue(test_engine.needs_service())

    def test_willoughby_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        test_engine = willoughby_engine.WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertFalse(test_engine.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)

        test_battery = spindler_battery.SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        self.assertTrue(test_battery.needs_service())

    def test_spindler_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        test_battery = spindler_battery.SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        self.assertFalse(test_battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        test_battery = spindler_battery.SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        self.assertTrue(test_battery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        test_battery = nubbin_battery.NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        self.assertFalse(test_battery.needs_service())

class TestCarriganTire(unittest.TestCase):
    def test_carrigan_tire_should_be_serviced(self):
        wear_sensors = [0.8, 0.9, 0.7, 0.7]

        test_tire = carrigan_tire.CarriganTire(wear_sensors=wear_sensors)
        self.assertTrue(test_tire.needs_service())

    def test_carrigan_tire_should_not_be_serviced(self):
        wear_sensors = [0.6, 0.4, 0.8, 0.5]

        test_tire = carrigan_tire.CarriganTire(wear_sensors=wear_sensors)
        self.assertFalse(test_tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_octoprime_tire_should_be_serviced(self):
        wear_sensors = [0.8, 0.8, 0.7, 0.7]

        test_tire = octoprime_tire.OctoprimeTire(wear_sensors=wear_sensors)
        self.assertTrue(test_tire.needs_service())

    def test_octoprime_tire_should_not_be_serviced(self):
        wear_sensors = [0.1, 0.1, 0.1, 0.1]

        test_tire = octoprime_tire.OctoprimeTire(wear_sensors=wear_sensors)
        self.assertFalse(test_tire.needs_service())

if __name__ == '__main__':
    unittest.main()
