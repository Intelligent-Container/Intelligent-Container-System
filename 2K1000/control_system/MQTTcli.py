import paho.mqtt.client as mqtt
import ssl


class MQTTClient:
    def __init__(self, client_id, username, password, server, port, cafile):
        self.client = mqtt.Client(client_id=client_id)

        #绑定回调函数
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        #设置用于验证的用户名和密码（看服务器需不需要）
        self.client.username_pw_set(username, password)

        # 设置用于验证的ssl认证文件（看服务器需不需要）
        ssl_context = ssl.create_default_context()
        ssl_context.load_verify_locations(cafile=cafile)

        self.client.tls_set_context(ssl_context)

        # 设置遗嘱消息(可用于下线提醒)
        self.client.will_set(topic="WillMsg", payload="Off Online！Connection Closed abnormally..!", qos=0, retain=False)

        #客户端开始连接
        self.client.connect(server, port, 60)

    # 连接成功的回调函数，自己再写个连接失败的回调函数吧（应对异常处理）
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
            # 想要订阅的主题，如果只订阅一个，可以自行改写到初始化参数里方便使用
            client.subscribe("testtopic")
            client.subscribe("WillMsg")
            # 给订阅的主题打个招呼（非必要，但可用于上线提醒）
        else:
            print("Connection failed with code", rc)

    def on_message(self, client, userdata, msg):#接受消息回调函数
        pass
        # print(msg.topic + " " + str(msg.payload.decode()))

    def send_message(self, topic, message):#发送主题内容
        self.client.publish(topic, message)

    def start_loop(self):#开启监听与回调循环
        self.client.loop_forever()


if __name__ == '__main__':
    client = MQTTClient(
        client_id="emqx_xavier",
        username="xavier",
        password="xavier",
        server="i1b4a003.ala.cn-hangzhou.emqxsl.cn",
        port=8883,
        cafile="emqxsl-ca.crt"
    )

    client.send_message("testtopic", "Hello from object!")#这是外部使用发送主题内容的调用方法

    client.start_loop()
    #start_loop（）是循环，后面是执行不到的
