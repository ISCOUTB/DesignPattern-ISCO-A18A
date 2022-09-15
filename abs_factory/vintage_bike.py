from abs_factory.bike import Bike


class VintageBike(Bike):

  def turn(self) -> str:
      return "Turn really slowly..."

  def honk(self) -> str:
      return "Honk quietly..."