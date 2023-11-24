pontuacoes_personagens = [
    [85, 90, 75, 60],
    [65, 34, 87, 90],
    [75, 66, 54, 76]
]

num_atributos = len(pontuacoes_personagens[0])

num_personagens = len(pontuacoes_personagens)

medias_atributos = [0] * num_atributos

for i in range(num_atributos):
    total = 0
    for j in range(num_personagens):
        total += pontuacoes_personagens[j][i]
        medias_atributos[i] = total / num_personagens

for i, media in enumerate(medias_atributos):
    print(f"Média do atributo {i + 1}: {media}")
