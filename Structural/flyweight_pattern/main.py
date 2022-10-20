from Structural.flyweight_pattern.flyweight_factory import FlyweightFactory


def add_doc(factory: FlyweightFactory, isbn: str, title:str, autor: str, editorial: str, year: int) -> None:
    print("\n\nClient: Adding a document to database.")
    flyweight = factory.get_flyweight([isbn, title, autor])
    # The client code either stores or calculates extrinsic state and passes it
    # to the flyweight's methods.
    flyweight.operation([editorial, year])


if __name__ == "__main__":
    """
    The client code usually creates a bunch of pre-populated flyweights in the
    initialization stage of the application.
    """

    factory = FlyweightFactory([
        ["978-1449331818", "Learning JavaScript Design Patterns", "Addy Osmani"],
        ["978-0201633610", "Design Patterns: Elements of Reusable Object-Oriented Software", "Richard Helm "],
    ])

    factory.list_flyweights()

    add_doc(factory, "978-9332555402", "Design Patterns", "Erich Gamma", "Person", 2015)
    add_doc(factory, "978-9332555402", "Design Patterns", "Erich Gamma", "O'Reilly", 2015)
    print("\n")

    factory.list_flyweights()