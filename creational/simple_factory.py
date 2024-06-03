from abc import ABC, abstractmethod
from random import choice


class Vehicle(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class Car_Lux(Vehicle):
    def buscar_cliente(self) -> None:
        print(f'{self.__class__.__name__} está buscando o cliente')


class CarPop(Vehicle):
    def buscar_cliente(self) -> None:
        print(f'{self.__class__.__name__} está buscando o cliente')


class VehicleFactory:
    @staticmethod
    def get_car(tipo: str) -> Vehicle | None:
        if tipo == 'luxo':
            return Car_Lux()
        elif tipo == 'pop':
            return CarPop()
        else:
            return None


if __name__ == '__main__':
    cars = ['luxo', 'pop']
    for i in range(10):
        choices: str = choice(cars)
        car = VehicleFactory.get_car(choices)
        car.buscar_cliente()
