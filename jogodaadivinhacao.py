import random

print("Bem-vindo ao jogo de adivinhação!")


print("Escolha o nível de dificuldade:")
print("1 - Fácil (0 a 50)")
print("2 - Normal (0 a 100)")
print("3 - Difícil (0 a 500)")
print("4 - Lendário (0 a 5000)")

opcao = input("Digite o número correspondente ao nível: ")


if opcao == '1':
    limite = 50
elif opcao == '2':
    limite = 100
elif opcao == '3':
    limite = 500
elif opcao == '4':
    limite = 5000
else:
    print("Opção inválida! O nível normal será usado por padrão.")
    limite = 100

numero_secreto = random.randint(0, limite)
tentativas = 0

while True:
    tentativa = input(f"Adivinhe o número entre 0 e {limite}: ")
    
    if not tentativa.isdigit():
        continue

    tentativa = int(tentativa)
    tentativas += 1

    if tentativa < numero_secreto:
        print("Muito baixo!")
    elif tentativa > numero_secreto:
        print("Muito alto!")
    else:
        print(f"Acertou em {tentativas} tentativas.")
        break
