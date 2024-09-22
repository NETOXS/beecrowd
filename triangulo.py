varetas = []

def registrar_varetas(n = 4):
    A,B,C,D = [int(x) for x in input().split()]
    varetas.append(A)
    varetas.append(B)
    varetas.append(C)
    varetas.append(D)
    
def checar_triangulo(lista):
    ordenadas = []
    ordenadas = sorted(varetas)
    if ordenadas[0] + ordenadas[1] > ordenadas[2] or ordenadas[0] + ordenadas[1] > ordenadas[3] or ordenadas[1] + ordenadas[2] > ordenadas[3]:
        return "S"
    else:
        return "N"


registrar_varetas()
print(checar_triangulo(varetas))


