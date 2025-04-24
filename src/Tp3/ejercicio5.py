# Producto
class Avion:
    def __init__(self):
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar_partes(self):
        print("Avión construido con:")
        for parte in self.partes:
            print(f" - {parte}")

# Builder abstracto
class AvionBuilder:
    def __init__(self):
        self.avion = Avion()

    def construir_body(self):
        self.avion.agregar_parte("Body")

    def construir_turbinas(self):
        self.avion.agregar_parte("Turbina izquierda")
        self.avion.agregar_parte("Turbina derecha")

    def construir_alas(self):
        self.avion.agregar_parte("Ala izquierda")
        self.avion.agregar_parte("Ala derecha")

    def construir_tren_aterrizaje(self):
        self.avion.agregar_parte("Tren de aterrizaje")

    def obtener_avion(self):
        return self.avion

# Director
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_avion_completo(self):
        self.builder.construir_body()
        self.builder.construir_turbinas()
        self.builder.construir_alas()
        self.builder.construir_tren_aterrizaje()
        return self.builder.obtener_avion()

# Prueba
builder = AvionBuilder()
director = Director(builder)
avion = director.construir_avion_completo()
avion.mostrar_partes()
