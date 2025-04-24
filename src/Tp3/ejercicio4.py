from abc import ABC, abstractmethod

# Producto base
class Factura(ABC):
    def __init__(self, importe):
        self.importe = importe

    @abstractmethod
    def mostrar_factura(self):
        pass

# Productos concretos
class FacturaResponsable(Factura):
    def mostrar_factura(self):
        print(f"Factura A - IVA Responsable. Total: ${self.importe:.2f}")

class FacturaNoInscripto(Factura):
    def mostrar_factura(self):
        print(f"Factura C - IVA No Inscripto. Total: ${self.importe:.2f}")

class FacturaExento(Factura):
    def mostrar_factura(self):
        print(f"Factura E - IVA Exento. Total: ${self.importe:.2f}")

# Factory
class FacturaFactory:
    @staticmethod
    def crear_factura(importe, condicion):
        if condicion == "responsable":
            return FacturaResponsable(importe)
        elif condicion == "no_inscripto":
            return FacturaNoInscripto(importe)
        elif condicion == "exento":
            return FacturaExento(importe)
        else:
            raise ValueError("Condición impositiva no reconocida")

# Prueba
factura1 = FacturaFactory.crear_factura(1500, "responsable")
factura1.mostrar_factura()  # Factura A - IVA Responsable. Total: $1500.00

factura2 = FacturaFactory.crear_factura(800, "exento")
factura2.mostrar_factura()  # Factura E - IVA Exento. Total: $800.00
