
class Singleton:
    __data: object = None

    def __init__(self):
        pass

    @property
    def data(self):
        if self.__data is not None:
            self.__data = Singleton()
        return self.__data


instance1 = Singleton.data
instance2 = Singleton.data

print(instance1 == instance2)  # True
