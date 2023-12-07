def calcular_salario_liquido(salario_bruto):
    # Calculando descontos
    vr = 660
    va = 250
    desconto_inss = salario_bruto * 0.08  # 8% de desconto do INSS
    desconto_transporte = salario_bruto * 0.04  # 4% de desconto do vale transporte
    desconto_fixo1 = vr * 0.20  # 20% de R$660 DO VR
    desconto_fixo2 = va * 0.05  # 5% DO VA

    
    descontos_totais = desconto_inss + desconto_transporte + desconto_fixo1 + desconto_fixo2

   
    salario_liquido = salario_bruto - descontos_totais

 
    if 1700 <= salario_liquido <= 1999:
        nivel = "ESTAGIARIO"
    elif 2000 <= salario_liquido <= 2900:
        nivel = "TRAINEE"
    elif 2901 <= salario_liquido <= 4000:
        nivel = "JUNIOR"
    elif 4001 <= salario_liquido <= 10000:
        nivel = "PLENO"
    elif salario_liquido > 10001:
        nivel = "SENIOR"
    else:
        nivel = "PEDE DEMISSÃO E VAI PARA O ESTAGIO ESTA COMPENSANDO MAIS FINANCEIRAMENTE"

    return salario_liquido, nivel


salario = float(input("Digite o salário Bruto: "))  


salario_liquido, nivel = calcular_salario_liquido(salario)


print(f"O salário líquido é: R${salario_liquido:.2f}")
print(f"Nível do desenvolvedor: {nivel}")
#print(f"O salário total recebido com benefícios é de: R${salario_liquido + 660 + 250:.2f}")