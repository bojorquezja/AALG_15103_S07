class Caja:
    def __init__(self, nombre, soles, peso):
        self.nombre = nombre
        self.peso = peso
        self.soles = soles
    def relacion(self):
        return self.soles / self.peso

def mochila_voraz(cajas, capacidad):
    peso_total = 0
    soles_totales = 0
    print("\nCajas seleccionadas:")

    for caja in cajas:
        if peso_total + caja.peso <= capacidad:
            peso_total += caja.peso
            soles_totales += caja.soles
            print(f"{caja.nombre}: {caja.peso}Kg S/{caja.soles}")
        else:
            espacio_restante = capacidad - peso_total
            if espacio_restante > 0:
                peso_fraccion = caja.peso * espacio_restante / caja.peso
                soles_fraccion = caja.soles * espacio_restante / caja.peso
                peso_total += peso_fraccion
                soles_totales += soles_fraccion
                print(f"Fraccion de {caja.nombre}: {peso_fraccion}Kg S/{soles_fraccion}")

            print(f"Soles obtenidos: {soles_totales:.2f}")
            break


m = float(input("Ingrese el peso máximo de la mochila: "))
cajas = [
    Caja("H", 3, 3),  
    Caja("G", 1.8, 2),
    Caja("B", 3, 4),
    Caja("F", 2, 3),
    Caja("C", 3, 7),
    Caja("A", 4, 10),
    Caja("D", 2, 5),
    Caja("E", 1, 3)
]

mochila_voraz(cajas, m)