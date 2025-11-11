import paho.mqtt.client as mqtt

class Conexao_mqtt:
    def __init__(self, usuario = None, senha = None, topicos = dict()):
        self.usuario = usuario
        self.senha = senha
        self.topicos = topicos
        self.mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2) #Objeto para conexão com o broker AdafruitIO
        # Atribui os eventos de comunicação com seu respectivo método
        self.mqttc.on_message = self.on_message
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_publish = self.on_publish
        self.mqttc.on_subscribe = self.on_subscribe
        self.mqttc.username_pw_set(self.usuario, self.senha)
        self.mqttc.connect("io.adafruit.com", 1883)
        for elemento in self.topicos:
            if self.topicos[elemento] == 'subscribe':
                self.mqttc.subscribe(f"{self.usuario}/feeds/{elemento}", 0)


    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"rc: {reason_code}")
        
    def on_message(self, client, obj, msg):
        print(f"Nova mensagem: {msg.topic} {msg.qos}")
        print(f"Texto recebido: {msg.payload}")

    def on_publish(self, client, userdata, mid, reason_code, properties):
        print(f"ID da mensagem enviada: {mid}")

    def on_subscribe(self, client, userdata, mid, reason_code_list, properties):
        if reason_code_list[0].is_failure:
            print(f"Broker rejected you subscription: {reason_code_list[0]}")
        else:
            print(f"Broker granted the following QoS: {reason_code_list[0].value}")

    def on_log(self, client, obj, level, string):
        print(string)

if __name__ == "__main__":
    def imprime(client, obj, msg):
        print('Este é o método do cliente')
        print(f"Nova mensagem: {msg.topic} {msg.qos}")
        print(f"Texto recebido: {msg.payload.decode()}")
        
    mqttc = Conexao_mqtt("SeuUsuario",
                        "aio_...",
                        {"eca10.topico1":'subscribe'})
    mqttc.mqttc.on_message = imprime
    while True:
        mqttc.mqttc.loop()

    