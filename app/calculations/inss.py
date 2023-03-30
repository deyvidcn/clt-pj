# app/calculations/inss.py
def calcular_desconto_inss(salario):
    faixa1 = 1302.00
    faixa2 = 2571.29
    faixa3 = 3856.94
    faixa4 = 7507.49

    if salario <= faixa1:
        return salario * 0.075
    if salario <= faixa2:
        return faixa1 * 0.075 + (salario - faixa1) * 0.09
    if salario <= faixa3:
        return faixa1 * 0.075 + (faixa2 - faixa1) * 0.09 + (salario - faixa2) * 0.12
    if salario <= faixa4:
        return faixa1 * 0.075 + (faixa2 - faixa1) * 0.09 + (faixa3 - faixa2) * 0.12 + (salario - faixa3) * 0.14
    return 877.22