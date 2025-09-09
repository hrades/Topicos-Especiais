import flet as ft

def main(pagina: ft.Page):
    def enviar_dados(e):
        nome = campo_nome.value
        idade = campo_idade.value
        if nome and idade:
            saida.value = f"Olá, {nome}! Você tem {idade} anos."
        else:
            saida.value = "Por favor, preencha todos os campos."
        pagina.update()

    campo_nome = ft.TextField(label="Nome")
    campo_idade = ft.TextField(label="Idade")
    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_dados)
    saida = ft.Text()

    pagina.add(campo_nome, campo_idade, botao_enviar, saida)

ft.app(target=main)
