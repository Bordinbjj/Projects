def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"


def exponenciacao(a, b):
    return a ** b


print("Selecione a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Exponenciação")


escolha = input("Digite a opção (1/2/3/4/5): ")


if escolha in ['1', '2', '3', '4', '5']:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado:", adicao(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado:", divisao(num1, num2))
    elif escolha == '5':
        print("Resultado:", exponenciacao(num1, num2))
else:
    print("Escolha inválida")
    