# app/calculations/pj.py
def calcular_pj(salario_liquido, desconto_inss, desconto_irrf, vr, va):
    prov_mensal_ferias = salario_liquido * 1.3 / 12
    prov_mensal_fgts = salario_liquido * 0.08
    prov_mensal_1_40_fgts = prov_mensal_fgts * 1.4
    salario_13 = salario_liquido / 12
    parc_mensal_seguro_desemprego = 1800 / 12
    contador = 300
    imposto = 0.18

    rendimento_bruto_pj = (
                                  salario_liquido + desconto_inss + desconto_irrf + vr + va + prov_mensal_ferias + prov_mensal_fgts + prov_mensal_1_40_fgts + parc_mensal_seguro_desemprego + contador) * (
                                  1 + imposto)

    return {
        'salario_liquido': salario_liquido,
        'vr': vr,
        'va': va,
        'prov_mensal_ferias': prov_mensal_ferias,
        'prov_mensal_fgts': prov_mensal_fgts,
        'prov_mensal_1_40_fgts': prov_mensal_1_40_fgts,
        'salario_13': salario_13,
        'parc_mensal_seguro_desemprego': parc_mensal_seguro_desemprego,
        'contador': contador,
        'imposto': imposto,
        'rendimento_bruto_pj': rendimento_bruto_pj
    }