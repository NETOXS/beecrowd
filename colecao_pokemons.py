pokemons_capturados = []
pokemons_unicos = []

def registrar_pokemons(n):
    if n == 0:
        return 0
    else:
        pokemon = input()
        pokemons_capturados.append(pokemon)
        return registrar_pokemons(n-1)

def retirar_repetidos():
    for pokemon in pokemons_capturados:
        if pokemon not in pokemons_unicos:
            pokemons_unicos.append(pokemon)


n = int(input())
registrar_pokemons(n)
retirar_repetidos()
restantes = 151 - len(pokemons_unicos)
print(f"Falta(m) {restantes} pomekon(s) .")

 
        
