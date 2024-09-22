botas = []

def registrar_botas(casos):
    for i in range(casos):
        tamanho, lado = input().split()
        bota = (tamanho, lado)
        botas.append(bota)

casos = int(input())
registrar_botas(casos)
pares = 0

while botas:
    bota_atual = botas.pop(0)
    tamanho_atual, lado_atual = bota_atual
    lado_oposto = 'E' if lado_atual == 'D' else 'D'

    for bota in botas:
        if bota[0] == tamanho_atual and bota[1] == lado_oposto:
            pares += 1
            botas.remove(bota)  
            break

print(f"Número de pares: {pares}")