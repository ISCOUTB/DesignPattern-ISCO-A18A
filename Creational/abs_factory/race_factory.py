from abs_factory.abstract_factory import AbstractFactory
from abs_factory.bike import Bike
from abs_factory.car import Car
from abs_factory.race_bike import RaceBike
from abs_factory.race_car import RaceCar


class RaceFactory(AbstractFactory):

    def createCar(self) -> Car:
        return RaceCar()

    def createBike(self) -> Bike:
        return RaceBike()