from abc import ABC, abstractmethod

# Producto
class Hamburguesa:
    def __init__(self, metodo_entrega):
        self.metodo_entrega = metodo_entrega

    def entregar(self):
        print(f"Entrega por {self.metodo_entrega}")

# Creator abstracto
class HamburguesaFactory(ABC):
    @abstractmethod
    def crear_hamburguesa(self):
        pass

# Concrete Creators
class MostradorFactory(HamburguesaFactory):
    def crear_hamburguesa(self):
        return Hamburguesa("mostrador")

class RetiroFactory(HamburguesaFactory):
    def crear_hamburguesa(self):
        return Hamburguesa("retiro por cliente")

class DeliveryFactory(HamburguesaFactory):
    def crear_hamburguesa(self):
        return Hamburguesa("delivery")

# Uso
factory = DeliveryFactory()
hamburguesa = factory.crear_hamburguesa()
hamburguesa.entregar()  # Output: Entrega por delivery
