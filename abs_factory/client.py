from abs_factory.abstract_factory import AbstractFactory
from abs_factory.race_factory import RaceFactory
from abs_factory.vintage_factory import VintageFactory


def client_code(factory: AbstractFactory) -> None:
    car = factory.createCar()
    bike = factory.createBike()

    print(f"{bike.turn()}")
    print(f"{bike.honk()}", end="")


if __name__ == "__main__":
    print("Client: checks product style")
    client_code(RaceFactory())

    print("\n")

    print("Client: checks product style")
    client_code(VintageFactory())