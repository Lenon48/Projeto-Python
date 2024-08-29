#inicio da função escolha_servico()
def escolha_servico():
    print('--------------------MENU 1 DE 3 - Escolha o Serviço Desejado --------------------')
    while True:
        servico = input('Entre com o Serviço Desejado: \n' +
                        'DIG - Digitalização \n' +
                        'ICO - Impressão Colorida \n' +
                        'IBO - Impressão Preto e Branco \n' +
                        'FOT - Fotocópia \n' +
                        '>>')
        servico = servico.upper()
        servico = servico.strip()
        if servico == 'DIG':
            return 1.10
        if servico == 'ICO':
            return 1.00
        if servico == 'IBO':
            return 0.40
        if servico == 'FOT':
            return 0.20
        else:
            print('Escolha Inválida')
            continue # retorna para o início
#fim da função escolha_servico()

#inicio da função num_pagina()
def num_pagina():
    print('--------------------MENU 2 DE 3 - Escolha o Número de Páginas Desejado --------------------')
    while True:
        try:
            qtd_pagina = int(input('Qual Número de Páginas Deseja?'))
            if (qtd_pagina < 10):
                return qtd_pagina
            elif (10 <= qtd_pagina < 100):
                return qtd_pagina * 0.9 # equivalente a 10% de Desconto
            elif (100 <= qtd_pagina < 1000):
                return qtd_pagina * 0.85 # equivalente a 15% de Desconto
            elif (1000 <= qtd_pagina < 10000):
                return qtd_pagina * 0.8 # equivalente a 20% de Desconto
            else:
                print('Não aceitamos tantas páginas de uma vez')
        except ValueError:
            print('Por favor, digite um valor válido')
#fim da função num_pagina()

#inicio da função servico_extra()
def servico_extra():
    print('--------------------MENU 3 DE 3 - Serviços Adicionais--------------------')
    acumulador = 0
    while True:
        servico_adicional = input('Deseja adicionar mais algum serviço?: \n' +
                                  '1 - Encardenação Simples: R$ 10,00 \n' +
                                  '2 - Encardenação Capa Dura: R$ 25,00 \n' +
                                  '0 - Não Desejo Mais Nada \n' +
                                  '>>')
        if servico_adicional == '1':
            acumulador = acumulador + 10
        elif servico_adicional == '2':
            acumulador = acumulador + 25
        elif servico_adicional == '0':
            return acumulador
            continue #volta para inicio menu
        else:
            print('Por Favor, digite opção válida de serviço adicional')
#fim da função servico_extra()

#Inicio do Main
print('--------------------Bem Vindo a Copiadora do Lucas Lenon Rodrigues Bueno --------------------')
servico = escolha_servico()
qtd_pagina = num_pagina()
servico_adicional = servico_extra()
total = (servico * qtd_pagina) + servico_adicional
print('O total ficou: R$ {:.2f},(servico: R$ {:.2f}, qtd_pagina: R$ {:.2F}, servico_adicional: R$ {:.2f}) ' .format(total,servico,qtd_pagina,servico_adicional))

