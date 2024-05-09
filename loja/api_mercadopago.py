import mercadopago

public_key = 'TEST-d2334ef6-0019-4bca-a47b-cc181184e736'
token = 'TEST-3440970467492547-042814-c96783bae8a439725b90b1f91b4b8859-1065467798'
# obs: as credenciais de produção deverão substituir as de teste ao ser feito o deploy do site


def criar_pagamento(itens_pedido, link):
    sdk = mercadopago.SDK(token)

    itens = []
    for item in itens_pedido:
        nome_produto = item.item_estoque.produto.nome
        quantidade = int(item.quantidade)
        preco_unitario = float(item.item_estoque.produto.preco)
        itens.append({
            'title': nome_produto,
            'quantity': quantidade,
            'unit_price': preco_unitario,
        })

    preference_data = {
        'items': itens,
        'auto_return': 'all',
        'back_urls': {
            'success': link,
            'pending': link,
            'failure': link, }
    }

    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta['response']['init_point']
    id_pagamento = resposta['response']['id']
    return link_pagamento, id_pagamento
