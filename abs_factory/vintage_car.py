from abs_factory.car import Car


class VintageCar(Car):

    def accelerate(self) -> str:
        return "Accelerate really slowly...!"

    def stop(self) -> str:
        return "Stop really slowly..."