from abs_factory.car import Car


class RaceCar(Car):

    def accelerate(self) -> str:
        return "Accelerate really fast!"

    def stop(self) -> str:
        return "Stop really fast!"