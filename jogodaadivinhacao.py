import random

while True:
    print("Bem-vindo ao jogo de adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        tentativa = input("Adivinhe o número entre 1 e 100: ")
        
        if not tentativa.isdigit():
            print("Por favor, digite um número válido.")
            continue

        tentativa = int(tentativa)
        tentativas += 1

        if tentativa < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif tentativa > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break  
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar! Até a próxima.")
        break 