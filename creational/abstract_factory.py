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

class Car_LuxB(VehicleLuxo):
    def buscar_cliente(self) -> None:
        print(f'{self.__class__.__name__} está buscando o cliente')


class CarPopB(VehiclePopular):
    def buscar_cliente(self) -> None:
        print(f'{self.__class__.__name__} está buscando o cliente')


class MotoB(VehiclePopular):
    def buscar_cliente(self) -> None:
        print(f'{self.__class__.__name__} está buscando o cliente')


class VehicleFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_car_lux() -> VehicleLuxo | None: pass

    @staticmethod
    @abstractmethod
    def get_car_pop() -> VehiclePopular | None: pass
    
    @staticmethod
    @abstractmethod
    def get_moto() -> VehicleLuxo | VehiclePopular | None: pass

class BaixadaVehicle(VehicleFactory):
    @staticmethod
    def get_car_lux() -> VehiclePopular:
        return Car_LuxB()

    @staticmethod
    def get_car_pop() -> VehiclePopular:
        return CarPopB()
        
    @staticmethod
    def get_moto() -> VehiclePopular | VehicleLuxo:
        return MotoB()
        
class Filiais:
    def busca_clientes(self):
        for item in [BaixadaVehicle()]:
            car_lux = item.get_car_lux()
            car_pop = item.get_car_pop()
            bike = item.get_moto()
            vehicle: VehicleFactory = choice([car_lux, car_pop, bike])
            vehicle.buscar_cliente()

if __name__ == '__main__':
    companies = Filiais()
    companies.busca_clientes()
