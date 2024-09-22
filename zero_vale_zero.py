def verificar_zero(soma):
    soma = str(soma)
    soma = soma.replace('0','')
    return soma

continuar = True

while continuar == True:
    n1, n2 = [int(x) for x in input().split()]
    soma = n1 + n2
    if(n1 == 0 and n2 == 0 and soma == 0):
        continuar = False
    else:
        print(int(verificar_zero(soma)))








    
