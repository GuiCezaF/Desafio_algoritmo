

def herdeiros(Familia: list[dict]) -> str:
    result = [Familia[0]['nome']]

    def buscar_herdeiro(pai):
        herdeiros = [individuo['nome'] for individuo in Familia if individuo['pai'] == pai]
        for filho in herdeiros:
            result.append(filho)
            buscar_herdeiro(filho)

    buscar_herdeiro(Familia[0]['nome'])
    return ' -> '.join(result)



Familia = [
    {'nome': 'Eduardo', 'pai': None},
    {'nome': 'Lucas', 'pai': 'Eduardo'},
    {'nome': 'Pedro', 'pai': 'Lucas'},
    {'nome': 'João', 'pai': 'Pedro'},
]
print(herdeiros(Familia))

