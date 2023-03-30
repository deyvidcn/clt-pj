# app/routes.py

from flask import Blueprint, request, jsonify
from .calculations import calcular_desconto_inss, calcular_desconto_irrf, calcular_pj

bp = Blueprint('routes', __name__)

@bp.route('/calcular', methods=['POST'])
def calcular():
    try:
        data = request.get_json()

        salario = float(data['salario'])
        numero_dependentes = int(data['dependentes'])
        outros_descontos = float(data['outros_descontos'])

        desconto_inss = calcular_desconto_inss(salario)
        desconto_irrf = calcular_desconto_irrf(salario, desconto_inss, numero_dependentes)
        salario_liquido = salario - desconto_inss - desconto_irrf - outros_descontos

        vr = float(data['vr'])
        va = float(data['va'])

        result_clt = {
            'salario_bruto': salario,
            'numero_dependentes': numero_dependentes,
            'desconto_inss': desconto_inss,
            'outros_descontos': outros_descontos,
            'salario_liquido': salario_liquido,
            'vr': vr,
            'va': va
        }

        result_pj = calcular_pj(salario_liquido, desconto_inss, desconto_irrf, vr, va)

        return jsonify({"clt": result_clt, "pj": result_pj})

    except Exception as e:
        logger.exception("Erro ao processar a solicitação:")
        return jsonify({"error": str(e)}), 500