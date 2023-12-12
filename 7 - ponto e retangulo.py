class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        return print(f"\n{self.x}, {self.y}")

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def encontrarcentro(self, p):
        x_centro = (p.x + self.largura) / 2
        y_centro = (p.y + self.altura) / 2
        return Ponto(x_centro, y_centro)
    
    def alterar_retangulo(self, nova_l, nova_a):
        self.largura = nova_l
        self.altura = nova_a

    def imprimir_centro(self, v, ponto):
        return print(f"\nCoordenadas do centro do retangulo com vertice {v.x, v.y}, de largura {self.largura} e altura {self.altura}: {ponto.x}, {ponto.y}")
        
v1 = Ponto(1, 1)
r1 = Retangulo(6, 4)
centro1 = r1.encontrarcentro(v1)
r1.imprimir_centro(v1, centro1)

v2 = Ponto(1, 4)
r2 = Retangulo(13, 6)
centro2 = r2.encontrarcentro(v2)
r2.imprimir_centro(v2, centro2)

r1.alterar_retangulo(6, 2)
centro1 = r1.encontrarcentro(v1)
r1.imprimir_centro(v1, centro1)


