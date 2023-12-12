class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade = self.idade + 1
        
    def crescer(self, valor):
        if self.idade < 21:
            self.altura = self.altura + 0.05

    def engordar(self, novo_peso):
        self.peso += novo_peso
    
    def emagrecer(self, novo_peso):
        self.peso -= novo_peso

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)
    
    def retornar_imc(self):
        if self.calcular_imc() <= 18:
            print("\nVocê está abaixo do seu peso, precisa engordar\n")
        elif self.calcular_imc() >= 24:
            print("\nVocê está acima do seu peso, precisa emagrecer\n")
        else:
            print("\nVocê está no seu peso ideal\n")

pessoa1 = Pessoa("Hee", 19, 55, 1.58)
print(pessoa1.nome, " com ", pessoa1.idade, "tem ", pessoa1.altura, " de altura e pesa ",pessoa1.peso, "quilogramas")
print("\nIMC:", pessoa1.calcular_imc())
pessoa1.retornar_imc()
pessoa1.envelhecer()
pessoa1.crescer()
pessoa1.engordar(5)
print(pessoa1.nome, " com ", pessoa1.idade, "tem ", pessoa1.altura, " de altura e pesa ",pessoa1.peso, "quilogramas")
print("\nIMC:", pessoa1.calcular_imc())
pessoa1.retornar_imc()
pessoa1.envelhecer()
print(pessoa1.nome, " com ", pessoa1.idade, "tem ", pessoa1.altura, " de altura e pesa ",pessoa1.peso, "quilogramas")
print("\nIMC:", pessoa1.calcular_imc())
pessoa1.retornar_imc()