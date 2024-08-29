print('Bem Vindo a Loja de Gelados do Lucas Lenon Rodrigues Bueno')
print('---------------------Cardápio---------------------')
print('Tamanho | Cupuaçu (CP)  | Açaí (AC)  |')
print(' P      | R$ 10.00      | R$ 12.00   |')
print(' M      | R$ 15.00      | R$ 17.00   |')
print(' G      | R$ 19.00      | R$ 21.00   |')
print('---------------------------------------------------')
acumulador = 0
while True:
    sabor = input('Entre com o sabor desejado: (CP/AC:) ')
    sabor = sabor.upper()
    if sabor != 'CP' and sabor != 'AC':
        print('Sabor Inválido. Tente Novamente')
        continue  # se usuário digitar algo inválido, volta para o começo do while

    tamanho = input('Entre com o tamanho que deseja: P/M/G): ')
    tamanho = tamanho.upper()
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho Inválido. Tente Novamente')
        continue  # se usuário digitar algo inválido, volta para o começo do while

    if sabor == 'CP' and tamanho == 'P':
        print('Você escolheu o gelado P de Cupuaçu')
        acumulador = acumulador + 10  # pegue o valor que tinha no acumulador e some com 10

    elif sabor == 'CP' and tamanho == 'M':
        print('Você escolheu o gelado M de Cupuaçu')
        acumulador = acumulador + 15  # pegue o valor que tinha no acumulador e some com 15

    elif sabor == 'CP' and tamanho == 'G':
        print('Você escolheu o gelado G de Cupuaçu')
        acumulador = acumulador + 19  # pegue o valor que tinha no acumulador e some com 19

    elif sabor == 'AC' and tamanho == 'P':
        print('Você escolheu o gelado P de Açaí')
        acumulador = acumulador + 12  # pegue o valor que tinha no acumulador e some com 12

    elif sabor == 'AC' and tamanho == 'M':
        print('Você escolheu o gelado M de Açaí')
        acumulador = acumulador + 17  # pegue o valor que tinha no acumulador e some com 17

    elif sabor == 'AC' and tamanho == 'G':
        print('Você escolheu o gelado G de Açaí')
        acumulador = acumulador + 21  # pegue o valor que tinha no acumulador e some com 21

    pedir_mais = input('Deseja pedir mais algum Gelado (S/N)?: ')
    pedir_mais = pedir_mais.upper()  # problema de maiúscula e minúscula resolvido.
    if pedir_mais == 'S':
        continue
    else:
        print('O valor total a ser pago: R${:.2F}'.format(acumulador))
        break
