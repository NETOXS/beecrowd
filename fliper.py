P, R = [int(i) for i in input().split()]

if P == 1 and R == 0:
    saida = "B"
elif P == 0:
    saida = "C"
elif P == 1 and R == 1:
    saida = "A"

print(saida)