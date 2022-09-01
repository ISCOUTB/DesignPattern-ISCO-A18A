from abc import ABC, abstractmethod


class DeliveryService():
    """
	Delivery service which is extended by specific delivery method classes
	"""

    def __init__(self, frozen: bool = False) -> None:
        self.frozen = frozen

    @abstractmethod
    def deliver_product(self):
        pass

    def factory_method(self):
        """
		Factory method returning object of the class based on the boolean flag
		"""
        if self.frozen:
            return FrozenDeliveryService()
        else:
            return NonFrozenDeliveryService()

    def delivery_operation(self):
        # calling factory to fetch the right class for delivery operation
        service = self.factory_method()

        service.deliver_product()


class FrozenDeliveryService(DeliveryService):

    def deliver_product(self):
        """
		Instantiates FrozenProduct class object
		"""
        print("Client wants delivery of frozen product")
        FrozenProduct().operation()
        print("Delivering frozen product")


class NonFrozenDeliveryService(DeliveryService):

    def deliver_product(self):
        """
		Instantiates NonFrozenProduct class object
		"""
        print("Client wants delivery of non frozen product")
        NonFrozenProduct().operation()
        print("Delivering non-frozen product")


class Product(ABC):
    """
	Interface for product types
	"""

    @abstractmethod
    def operation(self):
        pass


class FrozenProduct(Product):
    """
	Concrete implimentation of the interface Product
	"""

    def operation(self):
        print("This is a frozen product")


class NonFrozenProduct(Product):
    """
	Concrete implimentation of the interface Product
	"""

    def operation(self):
        print("This is a non-frozen product")


if __name__ == '__main__':
    """
	Client code
	"""

    print("Client isn't aware of different types delivery services.")
    print("Only information needed from client is `frozen` boolean flag.")
    print("\n")
    print("Case 1: `frozen` boolean flag set to True")
    delivery = DeliveryService(frozen=True)
    delivery.delivery_operation()
    print("\n")
    print("Case 2: `frozen` boolean flag set to False")
    delivery = DeliveryService(frozen=False)
    delivery.delivery_operation()
