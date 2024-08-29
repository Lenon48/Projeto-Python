# Inicio das Variáveis Globais
lista_livro = []
id_global = 0
# Fim das Variáveis Globais

# Inicio da Função cadastrar_livro(id)
def cadastrar_livro(id):
    print('-------------------- Menu Cadastrar Livro -------------------- ')
    print('id do livro: {}'.format(id_global))
    nome = input('Por Favor, Entre com o Nome: ')
    autor = input('Por Favor, Entre com o Autor: ')
    editora = input('Por Favor, Entre com a Editora: ')
    dicionario_livro = {'id'        :   id,
                        'nome'      :   nome,
                        'autor'     :   autor,
                        'editora'   :   editora}
    lista_livro.append(dicionario_livro.copy())
# Fim da Função cadastrar_livro(id)

# Inicio da Função consultar_livro()
def consultar_livro(id):
    global livro
    print('-------------------- Menu Consultar Livro -------------------- ')
    while True:
        menu_consultar = input('\nEscolha a opção desejada:\n' +
                               '1- Consultar Todos\n' +
                               '2- Consultar por id\n' +
                               '3- Consultar por Autor\n' +
                               '4- Retornar ao Menu\n' +
                               '>>')
        if menu_consultar == '1':
           print('Você Escolheu a Opção Consultar Todos os Livros')
           for livro in lista_livro: # Livro Vai Varrer Toda a Lista de Livros
            print('----------------------------------------------')
            for key, value in livro.items(): # Varrer Todos os Conjuntos Chave e Valor do Dicionário Livro
              print('{}: {}'.format(key,value))
        elif menu_consultar == '2':
            print('Você Escolheu a Opção Consulta Por Id')
            id_desejado = int(input('Entre com a Id Desejada: '))
            for livro in lista_livro:
                if livro['id'] == id_desejado: #O Valor do Campo Id_Global Deste Ducionário é Igual o Valor Desejado
                    for key, value in livro.items():  # Varrer Todos os Conjuntos Chave e Valor do Dicionário Livro
                        print('{}: {}'.format(key, value))
        elif menu_consultar == '3':
            print('Você Escolheu a Opção Consultar por Autor')
            id_desejado = input('Entre com o Autor Desejado: ')
            for livro in lista_livro:
                if livro['autor'] == id_desejado:  # O Valor do Campo Id_Global Deste Ducionário é Igual o Valor Desejado
                    for key, value in livro.items():  # Varrer Todos os Conjuntos Chave e Valor do Dicionário Livro
                        print('{}: {}'.format(key, value))
                    print('-----------------------------------------')
        elif menu_consultar == '4':
            return  # Sai da Função Consultar Produto e Volta para o Main
        else:
            print('Opção Inválida. Tente Novamente')
            continue  # volta para o início do laço
# Fim da Função consultar_livro()

# Inicio da Função remover_livro()
def remover_livro(id):
    print('-------------------- Menu Remover Livro -------------------- ')
    id_desejado = int(input('Digite o Id do Livro a ser Removido: '))
    for livro in lista_livro:
        if livro['id'] == id_desejado:  # O Valor do Campo Id_Global Deste Ducionário é Igual o Valor Desejado
            lista_livro.remove(livro)
            print('Livro Removido')
# Fim da Função remover_livro()

# Inicio de Main
print('Bem-Vindo ao Controle de Livros de Lucas Lenon Rodrigues Bueno')
while True:
    print('-------------------- Menu Principal ------------------------- ')
    menu_principal = input('\nEscolha a opção desejada:\n' +
                           '1- Cadastrar Livro\n' +
                           '2- Consultar Livro(s)\n' +
                           '3- Remover Livro\n' +
                           '4- Encerrar Programa\n' +
                           '>>')
    if menu_principal == '1':
        id_global = id_global + 1
        cadastrar_livro(id_global)
    elif menu_principal == '2':
        consultar_livro(id)
    elif menu_principal == '3':
        remover_livro(id)
    elif menu_principal == '4':
        break # encerra o laço principal e o programa acaba
    else:
        print('Opção Inválida. Tente Novamente')
        continue # volta para o início do laço
# Fim de Main