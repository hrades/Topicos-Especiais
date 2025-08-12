from os import system
from time import sleep

def main_menu():
    print('- Gerenciador de Relacionamento com Clintes -')
    print('1 - Clientes')
    print('2 - Tarefas')
    print('3 - Marketing')
    print('4 - Fechar programa')

def tela_gerenciamento(escolha=str()):
    system('cls')
    print(f'Gerenciamento de {escolha}s')
    print(f'1 - Cadastrar {escolha}')
    print(f'2 - Consultar {escolha}')
    print(f'3 - Excluir {escolha}')
    print('4 - Voltar ao menu anterior')

def cadastrar(info=str(), lista_dados=list(), lista_textos=list()):
    print(f'- Cadastro de {info}')
    dado1 = input(lista_textos[0])
    dado2 = input(lista_textos[1])
    dados = [dado1, dado2]
    if len(lista_textos)==3:
        dado3 = input(lista_textos[2])
        dados.append(dado3)
    lista_dados.append(dados)

def consultar(lista_dados=list(), lista_textos=list()):
    if len(lista_dados)==0:
        print('Nenhuma informacao cadastrada')
        sleep(3)
        system('cls')
    else:
        system('cls')
        for item in lista_dados:
            print('')
            for ind in range(0,len(lista_textos)):
                print(f'{lista_textos[ind]}{item[ind]}')
        voltar = input('\nPressione Enter para voltar')

def excluir(lista_dados=list()):
    if len(lista_dados)==0:
        print('Nenhuma informacao cadastrada')
        sleep(3)
        system('cls')
    else:
        for c in range(0, len(lista_dados)):
            print(f'{c} - {lista_dados[c][0]}')
        exclusao = int(input('Escolha qual será excluído pelo número: '))
        if exclusao in range(0, len(lista_dados)):
            lista_dados.pop(exclusao)
        else:
            print('ERRO! Informação selecionada inexistente')
            sleep(3)

selecao = int()
opcao = int()
escolhas = [1, 2, 3, 4]
textos = ['','cliente','tarefa', 'campanha']

lista_clientes = list()
textos_clientes = ['Nome do cliente: ', 'Email do cliente: ', 'Telefone do cliente: ']

lista_tarefas = list()
textos_tarefas = ['Titulo da tarefa: ', 'Prioridade: ', 'Descrição da tarefa: ']

lista_campanhas = list()
textos_campanhas = ['Nome da campanha: ', 'Descrição da campanha: ']


while True:
    main_menu()
    selecao = int(input('Escolha uma opcao pelo numero: '))
    while selecao not in escolhas:
        print('Comando inválido! Digite novamente')
        selecao = int(input('Escolha uma opcao pelo numero: '))

    while selecao==1:
        tela_gerenciamento(textos[selecao])
        opcao = int(input('Escolha uma opcao pelo numero: '))
        while opcao not in escolhas:
            print('Comando inválido! Digite novamente')
            opcao = int(input('Escolha uma opcao pelo numero: '))
        if opcao==1:
            cadastrar(textos[selecao], lista_clientes, textos_clientes)
        elif opcao==2:
            consultar(lista_clientes, textos_clientes)
        elif opcao==3:
            excluir(lista_clientes)
        elif opcao==4:
            selecao = 0
            opcao = 0
            system('cls')

    while selecao==2:
        tela_gerenciamento(textos[selecao])
        opcao = int(input('Escolha uma opcao pelo numero: '))
        while opcao not in escolhas:
            print('Comando inválido! Digite novamente')
            opcao = int(input('Escolha uma opcao pelo numero: '))
        if opcao==1:
            cadastrar(textos[selecao], lista_tarefas, textos_tarefas)
        elif opcao==2:
            consultar(lista_tarefas, textos_tarefas)
        elif opcao==3:
            excluir(lista_tarefas)
        elif opcao==4:
            selecao = 0
            opcao = 0
            system('cls')

    while selecao==3:
        tela_gerenciamento(textos[selecao])
        opcao = int(input('Escolha uma opcao pelo numero: '))
        while opcao not in escolhas:
            print('Comando inválido! Digite novamente')
            opcao = int(input('Escolha uma opcao pelo numero: '))
        if opcao==1:
            cadastrar(textos[selecao], lista_campanhas, textos_campanhas)
        elif opcao==2:
            consultar(lista_campanhas, textos_campanhas)
        elif opcao==3:
            excluir(lista_campanhas)
        elif opcao==4:
            selecao = 0
            opcao = 0
            system('cls')
    
    if selecao==4:
        system('cls')
        fechar = input('Tem certeza que quer fechar? (s/n): ').lower()
        while fechar not in 'sn':
            system('cls')
            fechar = input('Opção inválida. Digite s para sair ou n para continuar no app: ')
        if fechar=='s':
            system('cls')
            break
        else:
            selecao==0
            system('cls')


