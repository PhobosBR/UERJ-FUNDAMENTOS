import random

codigo_secreto = random.randint(1, 100)
tentativas = 0
registro_nome = ""
registro_tentativas = 0

def exibir_menu():
    print("Bem-vindo à Convenção de Cultura Pop!")
    print("Menu Interdimensional de Opções:")
    print("1. Embarcar em uma Nova Missão")
    print("2. Explorar o último desafio")
    print("3. Abandonar a Convenção (Sair)")

def iniciar_novo_jogo():
    codigo_secreto = random.randint(1, 100)
    tentativas = 0
    print("Você embarcou em uma Nova Missão! Boa sorte.")
    return codigo_secreto, tentativas

def explorar_ultimo_desafio():
    if registro_nome:
        print(f"Nome do jogador: {registro_nome}")
        print(f"Número de tentativas no último jogo: {registro_tentativas}")
    else:
        print("Nenhum registro de jogo disponível.")

while True:
    exibir_menu()
    escolha = input("Escolha uma opção (1/2/3): ")
    if escolha == "1":
        iniciar_novo_jogo()
        nome_jogador = input("Digite o seu nome: ")
        registro_nome = nome_jogador
        while True:
            tentativa = input("Digite um número entre 1 e 100: ")
            if not tentativa.isdigit():
                print("Por favor, digite um número válido.")
                continue
            tentativa = int(tentativa)
            tentativas += 1
            if tentativa < codigo_secreto:
                print("O número secreto está em uma galáxia distante. Tente um número maior.")
            elif tentativa > codigo_secreto:
                print("O número secreto está em uma órbita mais elevada. Tente um número menor.")
            else:
                print(f"Parabéns, {nome_jogador}! Você decifrou o código em {tentativas} tentativas.")
                registro_tentativas = tentativas
                break
    elif escolha == "2":
        explorar_ultimo_desafio()
    elif escolha == "3":
        print("Obrigado por participar da Convenção da Cultura Pop! Até a próxima aventura.")
        break
    else:
        print("Essa dimensão não existe. Escolha uma opção válida (1/2/3).")
