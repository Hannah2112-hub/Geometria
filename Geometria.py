class Geometria:
    def area(self, ancho, alto=None):
        if alto is None:
            alto = ancho
        return ancho * alto

    def perimetro(self, ancho, alto=None):
        if alto is None:
            alto = ancho
        return 2 * (ancho + alto)

    def area_cuadrado(self, lado):
        return self.area(lado)

    def area_rectangulo(self, ancho, alto):
        return self.area(ancho, alto)

    def perimetro_cuadrado(self, lado):
        return self.perimetro(lado)

    def perimetro_rectangulo(self, ancho, alto):
        return self.perimetro(ancho, alto)


#Realizando pruebas
geo = Geometria()

def probar_cuadrado():
    print("---- PRUEBAS PARA CUADRADO ----")
    lado = 4
    print(f"Área del cuadrado (lado={lado}): {geo.area_cuadrado(lado)}")
    lado = 5
    print(f"Área del cuadrado (lado={lado}): {geo.area_cuadrado(lado)}")

    lado = 4
    print(f"Perímetro del cuadrado (lado={lado}): {geo.perimetro_cuadrado(lado)}")
    lado = 5
    print(f"Perímetro del cuadrado (lado={lado}): {geo.perimetro_cuadrado(lado)}")


def probar_rectangulo():
    print("---- PRUEBAS PARA RECTÁNGULO ----")
    ancho, alto = 4, 6
    print(f"Área del rectángulo (ancho={ancho}, alto={alto}): {geo.area_rectangulo(ancho, alto)}")
    ancho, alto = 3, 7
    print(f"Área del rectángulo (ancho={ancho}, alto={alto}): {geo.area_rectangulo(ancho, alto)}")

    ancho, alto = 4, 6
    print(
        f"Perímetro del rectángulo (ancho={ancho}, alto={alto}): {geo.perimetro_rectangulo(ancho, alto)}")
    ancho, alto = 3, 7
    print(
        f"Perímetro del rectángulo (ancho={ancho}, alto={alto}): {geo.perimetro_rectangulo(ancho, alto)}")


probar_cuadrado()
print()
probar_rectangulo()