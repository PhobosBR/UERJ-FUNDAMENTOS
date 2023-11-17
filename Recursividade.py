def decimal_para_binario_recursivo(numero_decimal, chamadas_restantes, resultado_binario=""):
    if numero_decimal > 0 and chamadas_restantes > 0:
        resto = numero_decimal % 2
        resultado_binario = str(resto) + resultado_binario
        numero_decimal //= 2
        chamadas_restantes -= 1
        return decimal_para_binario_recursivo(numero_decimal, chamadas_restantes, resultado_binario)
    elif chamadas_restantes == 0:
        return "Limite máximo de chamadas recursivas atingido."
    else:
        return resultado_binario


numero_decimal = 11
limite_chamadas = 5

resultado = decimal_para_binario_recursivo(numero_decimal, limite_chamadas)

print(f"A representação binária de {numero_decimal} é: {resultado}")
