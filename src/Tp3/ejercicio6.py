import copy

# Clase prototipo
class Documento:
    def __init__(self, contenido):
        self.contenido = contenido

    def clonar(self):
        return copy.deepcopy(self)

    def mostrar(self):
        print(f"Documento: {self.contenido}")

# Prueba
doc1 = Documento("Contrato original")
doc2 = doc1.clonar()
doc3 = doc2.clonar()

doc1.mostrar()  # Documento: Contrato original
doc2.mostrar()  # Documento: Contrato original
doc3.mostrar()  # Documento: Contrato original

# Verificación de independencia (cambio solo en uno)
doc2.contenido = "Contrato modificado"

print("\nDespués de modificar doc2:")
doc1.mostrar()  # Sigue siendo "Contrato original"
doc2.mostrar()  # Ahora es "Contrato modificado"
doc3.mostrar()  # Sigue siendo "Contrato original"
