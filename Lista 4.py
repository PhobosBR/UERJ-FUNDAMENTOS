matriz_portal = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

def verificar_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    if linhas != colunas:
        return False
    
    for i in range(linhas):
        for j in range(colunas):
            if i == j and matriz[i][j] != 1:
                return False
            elif i != j and matriz[i][j] != 0:
                return False
    return True
    
if verificar_matriz(matriz_portal):
    print("A matriz_portal é uma Matriz Identidade Intergaláctica!")
else:
    print("A matriz_portal não é uma Matriz Identidade Intergaláctiva.")