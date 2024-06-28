from typing import Any


class Singleton(type):
    _instances = {}
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls._instances[cls]
    

class Conexao(metaclass=Singleton):
    def __init__(self):
        self.conexao = True if super().__class__.__call__() else False
        print(f" {self.__class__.__name__} conected" if self.conexao else "Not conected")
    

connection = Conexao()

connection2 = Conexao()

print(connection == connection2)
