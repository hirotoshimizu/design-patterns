from abc import ABC, abstractmethod


class Implementation(ABC):
    @abstractmethod
    def implementation(self) -> None:
        pass


class ConcreteImplementationA(Implementation):
    def implementation(self) -> None:
        print("ConcreteImplementationA.implementation")


class ConcreteImplementationB(Implementation):
    def implementation(self) -> None:
        print("ConcreteImplementationB.implementation")


class Abstraction(ABC):
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation


class RefinedAbstractionA(Abstraction):
    def do_something(self) -> None:
        self.implementation.implementation()


class RefinedAbstractionB(Abstraction):
    def do_something_else(self) -> None:
        self.implementation.implementation()


def main() -> None:
    impl = ConcreteImplementationA()
    abstraction = RefinedAbstractionA(impl)
    abstraction.do_something()


if __name__ == "__main__":
    main()
