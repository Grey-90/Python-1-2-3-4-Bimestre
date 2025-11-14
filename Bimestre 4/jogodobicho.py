import random

jogo = ["Perdeu", "Ganhou", "Perdeu", "Perdeu", "Perdeu", "Ganhou", "P6erdeu"]
random.shuffle(jogo)


indice = int(input("Digite um número de 0 a 6:"))

print("Você:", jogo[indice])