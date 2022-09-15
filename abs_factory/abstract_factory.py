from __future__ import annotations
from abc import ABC, abstractmethod

from abs_factory.bike import Bike
from abs_factory.car import Car


class AbstractFactory(ABC):

    @abstractmethod
    def createCar(self) -> Car:
        pass

    @abstractmethod
    def createBike(self) -> Bike:
        pass


