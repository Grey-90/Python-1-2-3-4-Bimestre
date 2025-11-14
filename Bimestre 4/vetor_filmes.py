Filmes = ["O Poderoso Chefão", "Pulp Fiction", "O Bom, o Mau e o Feio", "A Lista de Schindler", "Bird Box"]

print("Os filmes são: ", Filmes)

filme = input("Escoha um filme: ")

if filme in Filmes:
    print("Você escolheu: ", filme)
else:
    print("O filme não está na lista.")