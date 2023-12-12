class bombacombustivel:
    def __init__(self, tipo, valorLitro, qtdCombustivel):
        self.tipo = tipo
        self.valorLitro = valorLitro
        self.qtdCombustivel = qtdCombustivel

    def abastecerporValor(self, valor):
        self.qtdCombustivel -= valor / self.valorLitro
        return print(f"\nValor pago: {valor}\nQuantidade de litros: {valor / self.valorLitro}, restam {self.qtdCombustivel} litros de {self.tipo}")

    def abastecerporLitro(self, litro):
        self.qtdCombustivel -= litro
        return print(f"\nValor pago: {litro * self.valorLitro}\nQuantidade de litros: {litro}, restam {self.qtdCombustivel} litros de {self.tipo}")

    def alterarValor(self, novovalor):
        self.valorLitro = novovalor

    def alterarCombustivel(self, novotipo, qtd):
        self.tipo = novotipo
        self.qtdCombustivel = qtd

    def alterarqtdCombustivel(self, novaqtd):
        self.qtdCombustivel = novaqtd

b1 = bombacombustivel("Gasolina", 6.75, 10000)
b2 = bombacombustivel("Diesel", 6.10, 10000)
b1.alterarValor(6.90)
b2.alterarValor(6.30)
b2.alterarCombustivel("Biodiesel", 20000)
b2.alterarqtdCombustivel(30000)
b1.abastecerporValor(14)
b1.abastecerporLitro(100)
b2.abastecerporValor(20)
b2.abastecerporLitro(100)
