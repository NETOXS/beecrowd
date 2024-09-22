def calcular_direcao(direcao, n):
    sentido = "N"
    for i in range (n):
            if sentido == 'N' and direcao[i] == 'D':
                sentido = 'L'
            elif sentido == 'L' and direcao[i] == 'D':
                  sentido = 'S'
            elif sentido == 'S' and direcao[i] == 'D':
                  sentido = 'O'
            elif sentido == 'O' and direcao[i] == 'D':
                  sentido = 'N'
            elif sentido == 'N' and direcao[i] == 'E':
                sentido = 'O'
            elif sentido == 'L' and direcao[i] == 'E':
                  sentido = 'N'
            elif sentido == 'S' and direcao[i] == 'E':
                  sentido = 'L'
            elif sentido == 'O' and direcao[i] == 'E':
                  sentido = 'S'
    return sentido

                    
direcao = input()
n = len(direcao)
print(calcular_direcao(direcao,n))



            
    



    

