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


class Moto(Vehicle):
    def buscar_cliente(self) -> None:
        print(f'{self.__class__.__name__} está buscando o cliente')


class VehicleFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_car(tipo: str) -> Vehicle: pass


class BaixadaVehicle(VehicleFactory):
    @staticmethod
    def get_car(tipo: str) -> Vehicle:
        if tipo == 'luxo':
            return Car_Lux()
        elif tipo == 'pop':
            return CarPop()
        else:
            return Moto()


if __name__ == '__main__':
    cars = ['luxo', 'pop', 'moto']
    for i in range(10):
        choices2: str = choice(cars)
        car2 = BaixadaVehicle.get_car(choices2)
        car2.buscar_cliente()
