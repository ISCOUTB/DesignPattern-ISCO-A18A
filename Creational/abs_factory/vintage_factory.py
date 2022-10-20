from abs_factory.abstract_factory import AbstractFactory
from abs_factory.bike import Bike
from abs_factory.car import Car
from abs_factory.vintage_bike import VintageBike
from abs_factory.vintage_car import VintageCar


class VintageFactory(AbstractFactory):
  def createCar(self) -> Car:
    return VintageCar()

  def createBike(self) -> Bike:
      return VintageBike()