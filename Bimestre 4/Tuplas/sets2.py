import random

lista1 = [random.randint(1, 10) for _ in range(5)]
lista2 = [random.randint(1, 10) for _ in range(5)]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

print(conjunto1)
print(conjunto2)

intersecao = conjunto1.intersection(conjunto2)

print(intersecao)