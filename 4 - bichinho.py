class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarnome(self, novonome):
        self.nome = novonome
        
    def alterarfome(self, novafome):
        self.fome = novafome

    def alterarsaude(self, novasaude):
        self.saude = novasaude
        
    def alteraridade(self, novaidade):
        self.idade = novaidade
        
    def humor(self): #implementar com niveis
        if self.fome == False and self.saude == True:
            print("Estou bem humorado(a)")
        elif self.fome == True and self.saude == True:
            print("Estou parcialmente bem humorado(a), me alimente, por favor")
        elif self.fome == False and self.saude == False:
            print("Estou parcialmente bem humorado(a), cuide da minha saude, por favor")
        else:
            print("MAL HUMORADO!!!!!!")

    def retornarnome(self):
        return print(f"Nome: {self.nome}")
        
    def retornarfome(self):
        return print(f"Fome: {self.fome}")

    def retornarsaude(self):
        return print(f"Saude: {self.saude}")

    def retornaridade(self):
        return print(f"Idade: {self.idade}")

b1 = Tamagushi("Thalyta", True, False, 5)
b1.retornarnome()
b1.retornaridade()
b1.humor()
b1.alterarnome("TT")
b1.alterarfome(False)
b1.humor()