from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine

from battery import spindler_battery
from battery import nubbin_battery

from car import Car

class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = capulet_engine.CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        car_battery = spindler_battery.SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        car = Car(engine=car_engine, battery=car_battery)
        return car

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = willoughby_engine.WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        car_battery = spindler_battery.SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        car = Car(engine=car_engine, battery=car_battery)
        return car

    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = sternman_engine.SternmanEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        car_battery = spindler_battery.SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        car = Car(engine=car_engine, battery=car_battery)
        return car

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = willoughby_engine.WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        car_battery = nubbin_battery.NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        car = Car(engine=car_engine, battery=car_battery)
        return car
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = capulet_engine.CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        car_battery = nubbin_battery.NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        car = Car(engine=car_engine, battery=car_battery)
        return car
