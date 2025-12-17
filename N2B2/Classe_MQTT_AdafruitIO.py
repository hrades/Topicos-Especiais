import paho.mqtt.client as mqtt

class conexao:
    def __init__(self, usuario = None, senha = None, topicos = dict()):
        self.usuario = usuario
        self.senha = senha
        self.topicos = topicos
        self.mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.mqttc.on_message = self.on_message
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_publish = self.on_publish
        self.mqttc.on_subscribe = self.on_subscribe
        self.mqttc.username_pw_set(self.usuario, self.senha)
        self.mqttc.connect("io.adafruit.com", 1883)
        for chave in self.topicos:
            if self.topicos[chave] == 'subscribe':
                self.mqttc.subscribe(f"{self.usuario}/feeds/{chave}", 0)

    def publicar(self, topico, texto):
        self.mqttc.publish(f"{self.usuario}/feeds/{topico}", texto)
    
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
    pass 

    