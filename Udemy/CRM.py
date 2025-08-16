from os import system
from time import sleep
import json # Biblioteca para trabalhar com arquivos JSON
import os

NOME_PASTA = 'Projeto CRM/dados' #Mudar o nome das pastas onde está o programa
NOME_ARQUIVO = 'dados_crm.json'
CAMINHO_ARQUIVO = os.path.join(NOME_PASTA, NOME_ARQUIVO)

def salvar_dados(clientes, tarefas, campanhas):
    # Pega o caminho da pasta a partir do caminho completo do arquivo
    pasta = os.path.dirname(CAMINHO_ARQUIVO)

    # Verifica se a pasta existe. Se não, cria a pasta.
    if not os.path.exists(pasta):
        os.makedirs(pasta)
        print(f"Pasta '{pasta}' criada com sucesso.")

    dados_para_salvar = {
        'clientes': clientes,
        'tarefas': tarefas,
        'campanhas': campanhas
    }
    # Usa a variável CAMINHO_ARQUIVO para abrir o arquivo no local certo
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(dados_para_salvar, arquivo, indent=4)
    print("\nDados salvos com sucesso!")
    sleep(1)

def carregar_dados():
    '''Carrega os dados do arquivo JSON de uma pasta específica'''
    
    try:
        # Usa a variável CAMINHO_ARQUIVO para ler o arquivo do local certo
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados.get('clientes', []), dados.get('tarefas', []), dados.get('campanhas', [])
    except FileNotFoundError:
        # Agora isso acontece se o arquivo ou a pasta não existirem
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
        # Salvar dados das listas no json
        if opcao in [1, 3]:
            salvar_dados(lista_clientes, lista_tarefas, lista_campanhas)
    system('cls')
    return 0

selecao = int()
opcao = int()
escolhas = ['1', '2', '3', '4']
textos = ['','cliente','tarefa', 'campanha']

# Carrega os dados do arquivo JSON ao iniciar o programa
lista_clientes, lista_tarefas, lista_campanhas = carregar_dados()

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
