n = int(input())
valores = []
def registrar_precos(n):
    if n == 0:
        return 0
    else:
        preco, gramas = map(float, input().split())
        valor = (preco / gramas) * 1000
        valores.append(valor)
        return registrar_precos(n-1)
    
registrar_precos(n)
print(f"{min(valores):.2f}")