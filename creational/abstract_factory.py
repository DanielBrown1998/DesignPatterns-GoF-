from abc import ABC, abstractmethod
from random import choice, random


class VehicleLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass

class VehiclePopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


if __name__ == '__main__':
    ...