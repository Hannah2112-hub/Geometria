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
