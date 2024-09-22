def registrar_strings():
    global A, B
    A, B = input().split()

def combinar_strings():
    nova_string = []
    len_A = len(A)
    len_B = len(B)
    max_len = max(len_A, len_B)  

    for i in range(max_len):
        if i < len_A:
            nova_string.append(A[i])  # Adiciona letra de A, se disponível
        if i < len_B:
            nova_string.append(B[i])  # Adiciona letra de B, se disponível

    string = ''.join(nova_string)
    strings.append(string)

strings = []
casos = int(input())
for i in range(casos):
    registrar_strings()
    combinar_strings()
for string in strings:
    print(string)