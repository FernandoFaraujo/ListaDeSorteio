print ("\nBem vindo! Insira os nomes à serem sorteados abaixo.\n")

lista_sorteio = []

while True:
    nomes = input("\nDigite os respectivos nomes: ")

    if nomes == ".":
        break
    
    lista_sorteio.append(nomes)

print ("\nLista criada:")

for nome in nomes:
    print (f"{lista_sorteio}\n")

import random

sorteio = lista_sorteio

escolha = random.choice(sorteio)

print (f"E o nome sorteado é: {escolha}\n")