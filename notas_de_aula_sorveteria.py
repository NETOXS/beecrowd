import datetime
vendas = []

#Definindo os preços das bolas e guardando os preços em um dicionário!
print("VAMOS CONSTRUIR O RELATÓRIO DE VENDAS DE HOJE!")
print("----------------")
uma_bola = float(input("Defina o preço do sorvete com uma bola: "))
duas_bolas = float(input("Agora com duas: "))
precos = {"uma_bola": uma_bola, "duas_bolas": duas_bolas}
data_hora_atual = datetime.datetime.now()

#registrando as vendas e suas respectivas informações na lista de dicionarios, vendas!
def registrar_vendas(tipo, quantidade, data = data_hora_atual.strftime("%Y-%m-%d")):
    if tipo.upper() == "UMA BOLA":
        valor = precos["uma_bola"] * quantidade
    elif tipo.upper() == "DUAS BOLAS":
        valor = precos["duas_bolas"] * quantidade
    vendas.append({"sorvete": tipo, "quantidade": quantidade, "valor": valor, "data": data})

#gerando o relatorio final das vendas!
def relatorio():
    vendas_diaria = 0
    valor_diario = 0
    print(f"O total de vendas realizadas foram de: {len(vendas)} vendas")
    for venda in vendas:
       vendas_diaria += venda["quantidade"]
    print(f"A quantidade de sorvetes vendidos foram de: {vendas_diaria} sorvetes")
    for venda in vendas:
        valor_diario += venda["valor"] 
    print(f"O valor total arrecadado foi de: {valor_diario} reais")

print("----------------")
print("Agora vamos registrar as vendas diárias!")
print("----------------")

#checando se houveram vendas no dia!
s_or_n = input("Algum sorvete foi vendido hoje? (S/N): ")
if s_or_n == "S":
    continuar = True   
    while continuar:
       print("----------------")
       tipo = input("Digite o tipo do sorvete vendido: ")
       quantidade = int(input("Agora a quantidade: "))
       registrar_vendas(tipo, quantidade)
       parar = input("Deseja registrar outra? (S/N): ")
       if parar.upper() == "N":
          print("----------------")
          print("Finalizando relatório...")
          break
elif s_or_n == "N":
    print("Sinto muito pelo dia ruim :(")

#se houveram vendas, imprimindo o relatório
if len(vendas) > 0:
   print("----------------")    
   print("RELATÓRIO:")
   print("----------------")
   relatorio()



