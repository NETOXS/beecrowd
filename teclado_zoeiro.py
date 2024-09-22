frases_erradas = []
frases_corrigidas = []
letras_corretas = []
letras_erradas = []

def armazenar_letras(n):
    if n == 0:
        return
    else:
        correta, errada = [str(x) for x in input().split()]
        letras_corretas.append(correta)
        letras_erradas.append(errada)
        armazenar_letras(n-1)

def armazenar_frases(m):
    if m == 0:
        return
    else:
        frase = input()
        frases_erradas.append(frase)
        armazenar_frases(m-1)

def trocar_letras(frases):
    for frase in frases:
        nova_frase = []
        for letra in frase:
            if letra in letras_erradas:
                indice = letras_erradas.index(letra)
                nova_frase.append(letras_corretas[indice])
            elif letra in letras_corretas:
                indice = letras_corretas.index(letra)
                nova_frase.append(letras_erradas[indice])
            else:
                nova_frase.append(letra)
        frases_corrigidas.append(''.join(nova_frase))

N, M = [int(x) for x in input().split()]

armazenar_letras(N)
armazenar_frases(M)
trocar_letras(frases_erradas)

for frase in frases_corrigidas:
    print(frase)