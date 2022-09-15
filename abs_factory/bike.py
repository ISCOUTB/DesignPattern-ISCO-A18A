from abc import ABC, abstractmethod


class Bike(ABC):

    @abstractmethod
    def turn(self) -> str:
        pass

    @abstractmethod
    def honk(self) -> str:
        pass
