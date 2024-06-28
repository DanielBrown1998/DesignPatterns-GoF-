# singleton com decorador (soluciona as confusões do __init__)
def singleton(the_class):
    instance = {}

    def get_class(*args, **kwargs):
        if the_class not in instance:
            instance[the_class] = the_class(*args, **kwargs)
        return instance[the_class]
    
    return get_class

@singleton
class Singleton2:

    def __init__(self) -> None:
        print("Eu sou chamado apenas uma vez!")


class Singleton(object): 
    
    _instance: object = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    instance1 = Singleton()
    instance2 = Singleton()

    print(instance1 is instance2)  # True

    instance3 = Singleton2()
    instance4 = Singleton2()

    print(instance3 is instance4)  # True
