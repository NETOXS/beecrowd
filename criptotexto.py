n = int(input())

for i in range(n):
    string = input()
    minusculas = [char for char in string if char.islower()]
    minusculas.reverse()  # Inverte a lista no lugar
    formatada = ''.join(minusculas)  # Junta a lista invertida em uma string
    print(formatada)