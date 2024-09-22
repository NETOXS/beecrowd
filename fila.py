def estado_final_fila():
    # Ler o valor de N
    N = int(input())

    # Ler os identificadores das pessoas na fila inicial
    fila_inicial = list(map(int, input().split()))

    # Ler o valor de M
    M = int(input())

    # Ler os identificadores das pessoas que saíram da fila
    pessoas_sairam = set(map(int, input().split()))  # Usando set para busca rápida

    # Construir a fila final excluindo quem saiu
    fila_final = [pessoa for pessoa in fila_inicial if pessoa not in pessoas_sairam]

    # Imprimir o estado final da fila
    print(' '.join(map(str, fila_final)))

# Executa a função
estado_final_fila()