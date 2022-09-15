from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def accelerate(self) -> str:
        pass

    @abstractmethod
    def stop(self) -> str:
        pass