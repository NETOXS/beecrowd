letter = input()
text = input().split()
quantidade = 0

for palavra in text:
    if letter in palavra:
        quantidade += 1

porcentagem = (quantidade / len(text)) * 100
float(porcentagem)
print(f"{round(porcentagem,1)}")