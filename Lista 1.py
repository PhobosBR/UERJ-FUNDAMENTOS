def encontrar_carta_mais_valiosa(cartas):
    carta_mais_valiosa = cartas[0]  

    for valor in cartas:
        if valor > carta_mais_valiosa:
            carta_mais_valiosa = valor

    return carta_mais_valiosa

cartas = [10, 5, 8, 15, 12, 20, 7]
mais_valiosa = encontrar_carta_mais_valiosa(cartas)

if mais_valiosa is not None:
    print(f"A carta mais valiosa tem o valor: {mais_valiosa}")
else:
    print("O álbum está vazio, não há cartas para avaliar.")
