class Macaco:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.lista = bucho

    def comer(self, comida):
        if isinstance(comida, str):
            self.lista.append(comida)
        elif isinstance(comida, Macaco):
            self.lista.append(f"Macaco {comida.nome}") # poderia passar comida.lista, pra constar as comidas do bucho do outro macaco
        else:
            print("\nNão dá pra comer isso não colega")

    def digerir(self):
        self.lista.clear()

    def verbucho(self):
        return self.lista

macaco1 = Macaco("Fred", [])
macaco2 = Macaco("Lucio", [])
macaco1.comer("banana")
macaco1.comer("maçã")
macaco2.comer("banana")
print(f"\nBucho do(a) macaco(a) {macaco1.nome} antes da digestão: {macaco1.verbucho()}")
macaco1.digerir()
print(f"\nBucho do(a) macaco(a) {macaco1.nome} depois da digestão: {macaco1.verbucho()}")
macaco2.comer(macaco1)
print(f"\nBucho do(a) macaco(a) {macaco2.nome} antes da digestão: {macaco2.verbucho()}")


