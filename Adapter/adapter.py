from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def operation(self) -> str:
        return f"Adapter operation"


class Adaptee:
    def specific_operation(self) -> str:
        print("Adaptee special_operation")


def client_code(target: Target) -> None:
    print(target.operation())


if __name__ == "__main__":
    adapter = Adapter(Adaptee())
    client_code(adapter)
