import datetime

medicamentos = [
    {
        "nome": "Paracetamol",
        "principio_ativo": "Paracetamol",
        "data_vencimento": "2024-12-01"
    },
    {
        "nome": "Ibuprofeno",
        "principio_ativo": "Ibuprofeno",
        "data_vencimento": "2025-06-15"
    },
    {
        "nome": "Amoxicilina",
        "principio_ativo": "Amoxicilina",
        "data_vencimento": "2023-10-30"
    },
    {
        "nome": "Dipirona",
        "principio_ativo": "Dipirona Sódica",
        "data_vencimento": "2024-08-20"
    },
    {
        "nome": "Aspirina",
        "principio_ativo": "Ácido Acetilsalicílico",
        "data_vencimento": "2026-01-05"
    },
    {
        "nome": "Loratadina",
        "principio_ativo": "Loratadina",
        "data_vencimento": "2025-09-10"
    }
]

def filtrar(char):
     filtrados = [medicamento for medicamento in medicamentos if medicamento["principio_ativo"][0] == char]
     print(filtrados)

filtrar("D")


def vencimento():
     hoje = datetime.today()
     vencimento = [medicamento for medicamento in medicamentos if medicamento["data_vencimento"] > hoje and medicamento["data_vencimento"] <= hoje + 30]
     return vencimento



