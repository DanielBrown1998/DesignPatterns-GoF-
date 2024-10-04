from abc import ABC, abstractmethod
from random import choice


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print(f"{__class__.__name__} está buscando o cliente.")
        print(f"{__class__.__name__} está levando o cliente para o destino.")
        print(f"{__class__.__name__} chegou ao destino.")
        print()


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print(f"{__class__.__name__} está buscando o cliente.")
        print(f"{__class__.__name__} está levando o cliente para o destino.")
        print(f"{__class__.__name__} chegou ao destino.")
        print()


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print(f"{__class__.__name__} está buscando o cliente.")
        print(f"{__class__.__name__} está levando o cliente para o destino.")
        print(f"{__class__.__name__} chegou ao destino.")
        print()

class VeiculoFactory:

    @staticmethod
    def get_veiculo(nome: str) -> Veiculo:
        if nome in 'Carro Popular':
            return CarroPopular()
        elif nome in 'Carro de Luxo':
            return CarroLuxo()
        elif nome in 'Moto':
            return Moto()
        else:
            raise ValueError('Veículo não existe.')

if __name__ == '__main__':
    for _ in range(10):
        veiculo = VeiculoFactory.get_veiculo(
            choice(
                ['Carro Popular', 'Carro de Luxo']
                )
            )
        veiculo.buscar_cliente()
