from os import system
from time import sleep
import json # Biblioteca para trabalhar com arquivos JSON

# --- NOVAS FUNÇÕES PARA SALVAR E CARREGAR DADOS ---

def salvar_dados(clientes, tarefas, campanhas):
    # Cria um dicionário para organizar todos os dados
    dados_para_salvar = {
        'clientes': clientes,
        'tarefas': tarefas,
        'campanhas': campanhas
    }
    # Abre o arquivo 'dados_crm.json' em modo de escrita ('w')
    # O 'with' garante que o arquivo será fechado corretamente no final
    with open('dados_crm.json', 'w', encoding='utf-8') as arquivo:
        # Usa json.dump para escrever o dicionário no arquivo indent=4 formata o arquivo para ser mais legível por humanos
        json.dump(dados_para_salvar, arquivo, indent=4)

def carregar_dados():
    '''Carrega os dados do arquivo JSON no início do programa
       Se o arquivo não existir, retorna listas vazias'''
    try:
        # Tenta abrir o arquivo 'dados_crm.json' em modo de leitura ('r')
        with open('dados_crm.json', 'r', encoding='utf-8') as arquivo:
            # Carrega o conteúdo do JSON para um dicionário
            dados = json.load(arquivo)
            # Retorna os dados das listas. .get() é usado para evitar erros caso uma das chaves (clientes, tarefas, etc.) não exista no arquivo.
            return dados.get('clientes', []), dados.get('tarefas', []), dados.get('campanhas', [])
    except FileNotFoundError:
        # Se o arquivo não for encontrado (primeira vez que o programa roda), retorna três listas vazias.
        return [], [], []

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
        sleep(2)
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
        exclusao = input('Escolha qual será excluído pelo número: ')
        resp = exclusao.isnumeric()
        while resp!=True:
            exclusao = input('ERRO! Sua resposta deve ser um número. \nEscolha qual será excluído pelo número: ')
            resp = exclusao.isnumeric()
        exclusao = int(exclusao)
        if exclusao in range(0, len(lista_dados)):
            lista_dados.pop(exclusao)
        else:
            print('ERRO! Informação selecionada inexistente')
            sleep(2)

def tela(selecao=int(), lista_dados=list(), lista_textos=list()):
    while True:
        system('cls')
        tela_gerenciamento(textos[selecao])
        opcao = input('Escolha uma opcao pelo numero: ')
        while opcao not in escolhas:
           print('Comando inválido! Digite novamente')
           opcao = input('Escolha uma opcao pelo numero: ')
        opcao = int(opcao)
        if opcao==1:
            cadastrar(textos[selecao], lista_dados, lista_textos)
        elif opcao==2:
            consultar(lista_dados, lista_textos)
        elif opcao==3:
            excluir(lista_dados)
        elif opcao==4:
            break
    system('cls')
    return 0

selecao = int()
opcao = int()
escolhas = ['1', '2', '3', '4']
textos = ['','cliente','tarefa', 'campanha']

# MODIFICAÇÃO: Carrega os dados do arquivo JSON ao iniciar o programa
lista_clientes, lista_tarefas, lista_campanhas = carregar_dados()

# Textos para os prompts de cadastro
textos_clientes = ['Nome do cliente: ', 'Email do cliente: ', 'Telefone do cliente: ']
textos_tarefas = ['Titulo da tarefa: ', 'Prioridade: ', 'Descrição da tarefa: ']
textos_campanhas = ['Nome da campanha: ', 'Descrição da campanha: ']

while True:
    main_menu()
    selecao = input('Escolha uma opcao pelo numero: ')
    while selecao not in escolhas:
        print('Comando inválido! Digite novamente')
        selecao = input('Escolha uma opcao pelo numero: ')
    selecao = int(selecao)
    if selecao==1:
        selecao = tela(selecao, lista_clientes, textos_clientes)
    elif selecao==2:
        selecao = tela(selecao, lista_tarefas, textos_tarefas)
    elif selecao==3:
        selecao = tela(selecao, lista_campanhas, textos_campanhas)
    # Salvar dados das listas no json
    if opcao in [1, 3]:
            salvar_dados(lista_clientes, lista_tarefas, lista_campanhas)
    
    elif selecao==4:
        system('cls')
        fechar = input('Tem certeza que quer fechar? (s/n): ').lower()
        if fechar == '':
            fechar='vazio'
        while fechar not in 'sn':
            system('cls')
            fechar = input('Opção inválida. Digite s para sair ou n para continuar no app: ')
            if fechar == '':
                fechar='vazio'
        if fechar=='s':
            system('cls')
            break
        else:
            selecao=0
            system('cls')
