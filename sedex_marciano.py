import math

L,A,P,R =[int(x) for x in input().split()]
diametro = R * 2
diagonal_caixa = math.sqrt(pow(L,2) + pow(A,2) + pow(P,2))

if diametro >= diagonal_caixa:
    print("S")
else:
    print("N")