voos = [{"numero_voo": "AA123", "cidade_origem": "São Paulo",
"horario_chegada": "10:30", "horario_partida": "11:00"},
{"numero_voo": "JJ456", "cidade_origem": "Rio de Janeiro",
"horario_chegada": "09:45", "horario_partida": "10:15"},
{"numero_voo": "BB789", "cidade_origem": "Brasília",
"horario_chegada": "08:20", "horario_partida": "08:50"},
{"numero_voo": "AA124", "cidade_origem": "São Paulo",
"horario_chegada": "14:00", "horario_partida": "14:30"},
{"numero_voo": "CC321", "cidade_origem": "Curitiba",
"horario_chegada": "12:10", "horario_partida": "12:40"}]

voos_filtrados = []

def filtrar_voos(origem, A, B, indice = 0):
    if len(voos) == indice:
        return 0
    else:
        if voos[indice]["cidade_origem"] == origem and A <= voos[indice]["horario_chegada"]  <= B:
            voos_filtrados.append(voos[indice])
    return filtrar_voos(origem, A, B, indice + 1)


origem = input("Digite o nome da cidade que deseja partir: ")
A, B = input("Digite o hoário de saída e chegada: ").split()
filtrar_voos(origem, A, B)
print(voos_filtrados)





