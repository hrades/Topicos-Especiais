import PySimpleGUI as sg

# Layout da janela
layout = [
    [sg.Text("Nome:"), sg.InputText(key='-NOME-')],
    [sg.Text("Idade:"), sg.InputText(key='-IDADE-')],
    [sg.Button("Enviar")],
    [sg.Text("", size=(40, 1), key='-OUTPUT-')]
]

# Criar a janela
janela = sg.Window("Formulário PySimpleGUI", layout)

# Loop de eventos
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    elif evento == "Enviar":
        nome = valores['-NOME-']
        idade = valores['-IDADE-']
        if nome and idade:
            janela['-OUTPUT-'].update(f"Olá, {nome}! Você tem {idade} anos.")
        else:
            janela['-OUTPUT-'].update("Por favor, preencha todos os campos.")

janela.close()
