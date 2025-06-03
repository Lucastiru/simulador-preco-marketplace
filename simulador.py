def calcular_preco(custo, imposto_pct, embalagem, frete, comissao_pct, margem_pct):
    imposto = custo * (imposto_pct / 100)
    custo_total = custo + imposto + embalagem
    preco_venda = (custo_total + frete) / (1 - (comissao_pct + margem_pct) / 100)

    comissao_valor = preco_venda * (comissao_pct / 100)
    custo_da_venda = imposto + embalagem + frete + comissao_valor
    lucro_liquido = preco_venda - custo_total - frete - comissao_valor
    margem_liquida = (lucro_liquido / preco_venda) * 100

    return {
        'preco_venda': round(preco_venda, 2),
        'lucro_liquido': round(lucro_liquido, 2),
        'margem_liquida': round(margem_liquida, 2),
        'custo_da_venda': round(custo_da_venda, 2)
    }
