def calcular_salario_base(salario_por_hora, horas_trabalhadas):
    salario_base = salario_por_hora * horas_trabalhadas
    return salario_base

def main():
    salario_por_hora = float(input("Digite o salário por hora: "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))

    salario_base = calcular_salario_base(salario_por_hora, horas_trabalhadas)
    print(f"O salário base é: R${salario_base:.2f}")

if __name__ == "__main__":
    main()
