# informativo de boas vindas.
print('Olá, Bem vindo a Loja do Lucas Lenon Rodrigues Bueno.')

valor_unitario: float = float(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com a quantidade de produtos: '))
desconto_produto = 0

if quantidade < 1000:  # if < 1000:
    desconto_produto = 0.00
elif 1000 <= quantidade < 3001:  # if (qtd>= 1000) and (qtd < 3001):
    desconto_produto = 0.03  # 3% = 0.03 || 100% = 1.00
elif 3000 <= quantidade < 5001:  # if (qtd>= 3000) and (qtd < 5001):
    desconto_produto = 0.05  # 5% = 0.05 || 100% = 1.00
else:
    desconto_produto = 0.08  # 8% = 0.08 || 100% = 1.00
# cálculo sem desconto
total_sem_desconto = valor_unitario * quantidade
print('O valor total SEM desconto é R$ {:.2f}.'.format(total_sem_desconto))
# cálculo com desconto
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print('O valor total COM desconto é R$ {:.2f}.'.format(total_com_desconto))
