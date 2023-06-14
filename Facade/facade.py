class Washing:
    """Subsystem # 1"""

    def wash(self):
        print("wash...")


class Rinsing:
    """Subsystem # 2"""

    def rinse(self):
        print("Rinsing...")


class Spining:
    """Subsystem # 3"""

    def rinse(self):
        print("Spining...")


class WashingMachine:
    """Facade"""

    def __init__(self) -> None:
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spining = Spining()

    def start_washing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spining.spin()


if __name__ == "__main__":
    washing_machine = WashingMachine()
    washing_machine.start_washing()
