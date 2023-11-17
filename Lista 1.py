def bubble_sort_max(cartas):
    n = len(cartas)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if cartas[j] > cartas[j + 1]:
                cartas[j], cartas[j + 1] = cartas[j + 1], cartas[j]

    return cartas[-1]

# Exemplo de uso:
cartas = [50, 30, 80, 120, 90]
maior_carta = bubble_sort_max(cartas)

if maior_carta is not None:
    print(f"A carta mais valiosa tem valor {maior_carta}.")
else:
    print("O álbum de cartas está vazio.")
