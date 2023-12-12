class TV:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def mudarcanal(self, novocanal):
        if 0 < novocanal <=100:
            self.canal = novocanal
        else:
            print("canal invalido")
            canal = int(input("\nEscolha o canal:"))
            self.mudarcanal(canal)
            

    def aumentarvolume(self):
        if self.volume < 100 :
            self.volume += 10
        else:
            print("Volume máximo")

    def diminuirvolume(self):
        if self.volume > 0 and self.volume <=100:
            self.volume -= 5
        else:
            print("Volume mínimo")

tv = TV(1, 0)
canal = int(input("\nEscolha o canal:"))
tv.mudarcanal(canal)
resp = int(input("\nDeseja alterar o volume? \n1-Sim\n2-Não\n"))
while resp == 1:
    opc = int(input("\n1-AUMENTAR\n2-DIMINUIR\n3-SAIR\n"))
    if opc == 1:
        tv.aumentarvolume()
        print("\nVolume atual:",tv.volume)
    elif opc == 2:
        tv.diminuirvolume()
        print("\nVolume atual:",tv.volume)
    elif opc == 3:
        resp = 0
    else:
        print("opção inválida")

print(f"\nEstamos no canal {tv.canal}, com {tv.volume} de volume")


