não_saudaveis =["refrigerante", "bolo", "biscoitos recheados", "sorvetes", "salgadinhos"]
saudaveis = ["Abacate", "Morango", "amoras", "mirtilo", "brócolis"]

comida = input("Digite uma comida:")

if comida in saudaveis:
    print("Comida Saúdavel")
elif comida in não_saudaveis:
    print("Comida não Saúdavel.")
else:
    print("Comida não presente na lista")