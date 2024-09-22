consumo = int(input())

if consumo <=  10:
    conta = 7 
if consumo > 10 and consumo <= 30:
    conta = 7 + (consumo - 10)
if consumo > 30 and consumo <= 100:
    conta = 7 + 20 + ((consumo - 30) * 2)
if consumo > 100:
    conta = 7 + 20 + 140 + ((consumo - 100) * 5)

print(conta) 