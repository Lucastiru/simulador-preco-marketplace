def calcular_preco(custo, imposto_pct, embalagem, frete, comissao_pct, margem_pct):
    imposto = custo * (imposto_pct / 100)
    custo_total = custo + imposto + embalagem
    preco_venda = (custo_total + frete) / (1 - (comissao_pct + margem_pct) / 100)

    lucro_liquido = preco_venda - custo_total - frete - (preco_venda * (comissao_pct / 100))
    margem_liquida = (lucro_liquido / preco_venda) * 100

    return {
        'preco_venda': round(preco_venda, 2),
        'lucro_liquido': round(lucro_liquido, 2),
        'margem_liquida': round(margem_liquida, 2)
    }
