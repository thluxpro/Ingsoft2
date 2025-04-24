from abc import ABC, abstractmethod

# Productos abstractos
class Boton(ABC):
    @abstractmethod
    def dibujar(self):
        pass

class Ventana(ABC):
    @abstractmethod
    def mostrar(self):
        pass

# Productos concretos para Windows
class BotonWindows(Boton):
    def dibujar(self):
        print("Dibujando botón estilo Windows")

class VentanaWindows(Ventana):
    def mostrar(self):
        print("Mostrando ventana estilo Windows")

# Productos concretos para macOS
class BotonMac(Boton):
    def dibujar(self):
        print("Dibujando botón estilo Mac")

class VentanaMac(Ventana):
    def mostrar(self):
        print("Mostrando ventana estilo Mac")

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def crear_boton(self):
        pass

    @abstractmethod
    def crear_ventana(self):
        pass

# Factories concretas
class WindowsFactory(GUIFactory):
    def crear_boton(self):
        return BotonWindows()

    def crear_ventana(self):
        return VentanaWindows()

class MacFactory(GUIFactory):
    def crear_boton(self):
        return BotonMac()

    def crear_ventana(self):
        return VentanaMac()

# Cliente
def crear_interfaz(factory):
    boton = factory.crear_boton()
    ventana = factory.crear_ventana()
    boton.dibujar()
    ventana.mostrar()

# Uso
print("Interfaz Windows:")
crear_interfaz(WindowsFactory())

print("\nInterfaz Mac:")
crear_interfaz(MacFactory())
