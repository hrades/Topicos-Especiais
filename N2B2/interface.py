import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from Classe_MQTT_AdafruitIO import conexao
from banco_de_dados import banco_dados

class aplicativo:
    def __init__(self, janela):
        self.master = janela
        self.conexao = conexao( usuario="usuario", senha="senha", topicos={"campo.umidade":"subscribe"})
        self.conexao.mqttc.on_message = self.nova_mensagem
        self.conexao.mqttc.on_connect = self.acao_conexao
        self.banco_dados = banco_dados()
        self.master.after(1500, self.acao_tempo_conexao)

        # Interface
        self.frm_dados_sensor = ttk.LabelFrame(self.master, text="Cadastrar novo sensor")
        self.txb_id = ttk.Entry(self.frm_dados_sensor)
        self.txb_localizacao = ttk.Entry(self.frm_dados_sensor)
        self.txb_profundidade = ttk.Entry(self.frm_dados_sensor)
        self.btn_cadastrar = ttk.Button(self.frm_dados_sensor, text="\nCadastrar\n", command=self.cadastrar_sensor)

        self.frm_leitura = ttk.LabelFrame(self.master, text="Enviar leitura de umidade")
        self.txb_id_leitura = ttk.Entry(self.frm_leitura)
        self.txb_umidade = ttk.Entry(self.frm_leitura)
        self.btn_enviar = ttk.Button(self.frm_leitura, text="Enviar", command=self.enviar_leitura)

        self.lbl_ultima_msg = ttk.Label(self.master, text="Aguardando leitura...")

        # Layout
        self.frm_dados_sensor.pack(expand=True, fill="both", padx=4, pady=4)
        ttk.Label(self.frm_dados_sensor, text="ID do sensor").grid(row=0, column=0, sticky="e")
        self.txb_id.grid(row=0, column=1, sticky="ew")
        ttk.Label(self.frm_dados_sensor, text="Localização").grid(row=1, column=0, sticky="e")
        self.txb_localizacao.grid(row=1, column=1, sticky="ew")
        ttk.Label(self.frm_dados_sensor, text="Profundidade (cm)").grid(row=2, column=0, sticky="e")
        self.txb_profundidade.grid(row=2, column=1, sticky="ew")
        self.btn_cadastrar.grid(row=0, column=2, padx=4, pady=4, rowspan=3)

        self.frm_leitura.pack(expand=True, fill="both", padx=4, pady=4)
        ttk.Label(self.frm_leitura, text="ID do sensor").grid(row=0, column=0, sticky="e")
        self.txb_id_leitura.grid(row=0, column=1, sticky="ew")
        ttk.Label(self.frm_leitura, text="Umidade (%)").grid(row=1, column=0, sticky="e")
        self.txb_umidade.grid(row=1, column=1, sticky="ew")
        self.btn_enviar.grid(row=0, column=2, rowspan=2, sticky="ns", padx=4, pady=4)

        self.lbl_ultima_msg.pack(anchor="w", padx=4)

    def acao_tempo_conexao(self):
        self.master.after(2500, self.acao_temporizador)
        self.conexao.mqttc.loop_read()

    def acao_temporizador(self):
        self.master.after(1000, self.acao_temporizador)
        self.conexao.mqttc.loop_read()

    def acao_conexao(self, client, userdata, flags, reason_code, properties):
        self.master.title(f"Status da conexão: {reason_code}")
        if reason_code == "Success":
            self.master.after(1000, self.acao_temporizador)

    def nova_mensagem(self, client, obj, msg):
        self.lbl_ultima_msg.configure(text=f"Mensagem recebida: {msg.payload}")

    def cadastrar_sensor(self):
        conexao_mongo = banco_dados()
        id_sensor = self.txb_id.get()
        loc = self.txb_localizacao.get()
        cm = self.txb_profundidade.get()
        documento = {"_id": id_sensor,
                     "localizacao": loc,
                     "profundidade_cm": cm}
        try:
            conexao_mongo.inserir_registro(documento)
        except:
            messagebox.showerror('Erro!', 'Ocorreu um erro.\nO documento não foi inserido')


    def enviar_leitura(self):
        id_sensor = self.txb_id_leitura.get
        umidade = self.txb_umidade.get
        hora = datetime.time()
        msg = f"SENSOR{id_sensor};{umidade};{hora}"
        try:
            self.conexao.publicar("campo.umidade", msg)
        except:
            messagebox.showerror('Erro!', 'Ocorreu um erro.\nA mensagem não foi publicada')

if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Monitoramento de Umidade")
    aplicativo(janela)
    ttk.Button(janela, text="Fechar", command=janela.destroy).pack(anchor="e", padx=4, pady=4)
    janela.mainloop()
