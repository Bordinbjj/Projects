def calcular_imc(peso, altura):
    
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso saudável"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"

def main():
    print("Calculadora de Índice de Massa Corporal (IMC)")
    peso = float(input("Digite o seu peso em quilogramas: "))
    altura = float(input("Digite a sua altura em metros: "))

    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")
    
    interpretacao = interpretar_imc(imc)
    print(f"Você está classificado como: {interpretacao}")

if __name__ == "__main__":
    main()
