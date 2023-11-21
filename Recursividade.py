def decimal_para_binario_recursivo(numero, limite_recursao=5):
    if limite_recursao == 0:
        print("Limite máximo de chamadas recursivas atingido. Abortando.")
        return ""
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return decimal_para_binario_recursivo(numero // 2, limite_recursao - 1) + str(numero % 2)

# Exemplo de uso
numero_decimal = 25
representacao_binaria = decimal_para_binario_recursivo(numero_decimal)
print(f"A representação binária de {numero_decimal} é: {representacao_binaria}")
