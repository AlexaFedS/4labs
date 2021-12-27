from abc import ABC, abstractmethod
from enum import Enum, auto

class Airplane(Enum):
    AirbusA220 = auto()
    AirbusA320 = auto()
    Boeing717 = auto()
    Boeing777X = auto()

class Where(Enum):
    Moscow = auto()
    Saratov = auto()
    Saint_Petersburg = auto()
    Samara = auto()
    Perm = auto()

class Wherefrom(Enum):
    Moscow = auto()
    Saratov = auto()
    Saint_Petersburg = auto()
    Samara = auto()
    Perm = auto()

class Company(Enum):
    Utair = auto()
    Aeroflot = auto()
    Pobeda = auto()
    Nordavia = auto()
    Komiavia = auto()

class Terminal(Enum):
    A = auto()
    B = auto()
    C = auto()
    D = auto()
    E = auto()


class Time(Enum):
    time12 = auto()
    time15 = auto()
    time18 = auto()
    time21 = auto()
    time00 = auto()

class Avia:
    def __init__(self, id):
        self.id = id
        self.airplane = None
        self.where = None
        self.wherefrom = None
        self.company = None
        self.terminal = None
        self.gate = None
        self.time = None
        self.cost = None

    def __str__(self):
        info: str = f"Avia ticket: {self.id} \n" \
                    f"{self.airplane} \n" \
                    f"{self.where} \n" \
                    f"{self.wherefrom} \n" \
                    f"{self.company} \n" \
                    f"{self.terminal} \n" \
                    f"{self.gate} \n" \
                    f"{self.time} \n" \
                    f"Cost: {self.cost} rub"
        return info

class Builder(ABC):

    @abstractmethod
    def add_airplane(self) -> None: pass

    @abstractmethod
    def add_where(self) -> None: pass

    @abstractmethod
    def add_wherefrom(self) -> None: pass

    @abstractmethod
    def add_company(self) -> None: pass

    @abstractmethod
    def add_terminal(self) -> None: pass

    @abstractmethod
    def add_time(self) -> None: pass

class MoscowPerm(Builder):
    def __init__(self):
        self.AviaTicket = Avia("MoscowPerm")
        self.AviaTicket.gate = 1
        self.AviaTicket.cost = 3566

    def add_airplane(self) -> None:
        self.AviaTicket.airplane = Airplane.AirbusA220

    def add_where(self) -> None:
        self.AviaTicket.where = Where.Perm

    def add_wherefrom(self) -> None:
        self.AviaTicket.wherefrom = Wherefrom.Moscow

    def add_company(self) -> None:
        self.AviaTicket.company = Company.Aeroflot

    def add_time(self) -> None:
        self.AviaTicket.time = Time.time18

    def add_terminal(self) -> None:
        self.AviaTicket.terminal = Terminal.C

    def get_lap(self) -> Avia:
        return self.AviaTicket

class PermSaratov(Builder):
    def __init__(self):
        self.AviaTicket = Avia("PermSaratov")
        self.AviaTicket.gate = 3
        self.AviaTicket.cost = 5000

    def add_airplane(self) -> None:
        self.AviaTicket.airplane = Airplane.Boeing777X

    def add_where(self) -> None:
        self.AviaTicket.where = Where.Saratov

    def add_wherefrom(self) -> None:
        self.AviaTicket.wherefrom = Wherefrom.Perm

    def add_company(self) -> None:
        self.AviaTicket.company = Company.Utair

    def add_time(self) -> None:
        self.AviaTicket.time = Time.time12

    def add_terminal(self) -> None:
        self.AviaTicket.terminal = Terminal.A

    def get_lap(self) -> Avia:
        return self.AviaTicket

class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_lap(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.add_airplane()
        self.builder.add_where()
        self.builder.add_wherefrom()
        self.builder.add_company()
        self.builder.add_terminal()
        self.builder.add_time()

def check_gate(id1):
    for al in (MoscowPerm, PermSaratov):
        director1 = Director()
        builder1 = al()
        director1.set_builder(builder1)
        director1.make_lap()
        AviaTicket1 = builder1.get_lap()
        if AviaTicket1.id == id1:
            return AviaTicket1.gate

def check_sum(x):
    for al in (MoscowPerm, PermSaratov):
        director1 = Director()
        builder1 = al()
        director1.set_builder(builder1)
        director1.make_lap()
        AviaTicket1 = builder1.get_lap()
        x += x + AviaTicket1.cost
    return x

if __name__ == "__main__":
    print("Объекты")
    director = Director()
    for el in (MoscowPerm, PermSaratov):
        builder = el()
        director.set_builder(builder)
        director.make_lap()
        AviaTicket = builder.get_lap()
        print(AviaTicket)
        print('------------------------------')
    id = "MoscowPerm"
    print(id, "gate: ", check_gate(id))
    x = 0
    print('sum = ', check_sum(x))
