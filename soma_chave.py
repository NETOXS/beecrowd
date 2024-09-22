lista = [1,2,1,4]
nomes = []
rep = 0




def soma_chave(lista, indice = 0):
    if len(lista) == indice:
        return 0
    else:
        return lista[indice] + soma_chave(lista,indice + 1)
    
def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n-1)

def registrar(n):
    if n == 0:
        return 0
    else:
        nome = input("Digite um nome: ")
        nomes.append(nome)
        return registrar(n-1)
    
def ocorrencias(lista,elemento, indice = 0):
    if len(lista) == indice:
        return 0
    else:
        if lista[indice] == elemento:
            rep = rep + 1
    return ocorrencias(lista,elemento,indice +1)
    


    
print(soma_chave(lista))
print(fatorial(3))
registrar(3)
print(nomes)
ocorrencias(lista,1)
print(rep)