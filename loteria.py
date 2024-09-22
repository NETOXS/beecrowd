import random

sorteio = []
aposta = []

def cadastrar_aposta():
    numeros = [int(x) for x in input().split()]
    aposta.append(numeros)

def gerar_sorteio():
    numeros = [int(x) for x in input().split()]
    sorteio.append(numeros)

gerar_sorteio()
cadastrar_aposta()
iguais = 0

for i in range(6):
    for j in range(6):
        if aposta[0][i] == sorteio[0][j]:
            iguais += 1

if iguais == 3:
    print("terno")
elif iguais == 4:
    print("quadra")
elif iguais == 5:
    print("quina")
elif iguais == 6:
    print("sena")
else:
    print("azar")



    
