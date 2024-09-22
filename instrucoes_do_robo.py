def registrar_movimentos(n):
    global movimentos
    if n == 0:
        return 0
    else:
        movimento = input()
        if movimento == "LEFT":
            movimentos = movimentos - 1
            armazenar_movimentos.append(-1)
        elif movimento == "RIGHT":
            movimentos = movimentos + 1
            armazenar_movimentos.append(1)
        else:
            numero = int(movimento[8])
            movimentos = movimentos + armazenar_movimentos[numero - 1]
            armazenar_movimentos.append(armazenar_movimentos[numero - 1])
        return registrar_movimentos(n-1)

casos = int(input())
    
for i in range(casos):
    inicial = 0
    movimentos = 0
    armazenar_movimentos = []

    n = int(input())
    registrar_movimentos(n)
    print(inicial + movimentos)


            
        
    