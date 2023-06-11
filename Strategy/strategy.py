from abc import ABC, abstractmethod


class Strategry(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class ConcreteStragegyA(Strategry):
    def execute(self) -> None:
        print("ConcreteStragegyA.execute")


class ConcreteStragegyB(Strategry):
    def execute(self) -> None:
        print("ConcreteStragegyB.execute")


class Context:
    def __init__(self, stragegy: Strategry) -> None:
        self.strategy = stragegy

    def do_something(self) -> None:
        self.strategy.execute()


def main() -> None:
    context = Context(stragegy=ConcreteStragegyA())
    context.do_something()


if __name__ == "__main__":
    main()
