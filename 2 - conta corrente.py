class contaCorrente:
  def __init__(self, nome, saldo, numero):
    self.nome = nome
    self.saldo = saldo
    self.numero = numero

  def alterarnome(self, novonome):
    self.nome = novonome

  def depositar(self, valor):
    self.saldo += valor

  def sacar(self, valor):
    if self.saldo >= valor:
      self.saldo -= valor
    else:
      print("Voce nao tem todo esse dinheiro, amigo")

  def versaldo(self):
    print(f"{self.nome}, com numero de conta {self.numero}, seu saldo é: {self.saldo}")

c1 = contaCorrente("Thalyta", 3, "12345-1")
c2 = contaCorrente("Philip", 10, "56789-1")
c1.alterarnome("Sofia")
c1.depositar(10)
c2.sacar(3)
c1.versaldo()
c2.versaldo()
