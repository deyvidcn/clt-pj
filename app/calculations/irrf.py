# app/calculations/irrf.py
def calcular_desconto_irrf(salario, inss, numero_dependentes):
    deducao_por_dependente = 189.59
    base_calculo = salario - inss - (numero_dependentes * deducao_por_dependente)

    if base_calculo <= 1903.98:
        return 0

    aliquotas = [
        [1903.99, 2826.65, 0.075, 142.80],
        [2826.66, 3751.05, 0.15, 354.80],
        [3751.06, 4664.68, 0.225, 636.13],
        [4664.69, None, 0.275, 869.36],
    ]

    for aliquota in aliquotas:
        if base_calculo > aliquota[0] and (aliquota[1] is None or base_calculo <= aliquota[1]):
            irrf = base_calculo * aliquota[2] - aliquota[3]

    return irrf


