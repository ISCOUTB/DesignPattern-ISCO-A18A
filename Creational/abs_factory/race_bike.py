from abs_factory.bike import Bike


class RaceBike(Bike):
  def turn(self) -> str:
      return "Turn really fast!"

  def honk(self) -> str:
      return "Honk loudly!"
