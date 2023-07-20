//客户端ID，起个名字（多个客户端通信时不要重复，或者直接写成随机）
const clientId = 'emqx_cloudelf'
//服务器连接地址和WebSocket TLS/SSL 端口：8084，后面的/mqtt可能是emqx要用的，要写上。
const host = 'wss://q24a314e.ala.cn-hangzhou.emqxsl.cn:8084/mqtt'
const options = {
    username: 'elf',
    password: '123456',
    keepalive: 30,
    clientId: clientId,
    protocolId: 'MQTT',
    protocolVersion: 4,
    clean: true,
    reconnectPeriod: 1000,
    connectTimeout: 30 * 1000,
    will: {
        topic: 'WillMsg',
        payload: 'Off Online！Connection Closed abnormally..!',
        qos: 0,
        retain: false
    },
    rejectUnauthorized: false
}

console.log('connecting mqtt client')
const client = mqtt.connect(host, options)


client.on('error', (err) => {
    console.log('Connection error: ', err)
    client.end()
})

client.on('reconnect', () => {
    console.log('Reconnecting...')
})

client.on('connect', () => {
    console.log('Client connected:' + clientId)
    client.subscribe('testtopic', {qos: 0})
    client.subscribe('WillMsg', {qos: 0})
    // client.publish('WillMsg', 'On Online!', {qos: 0, retain: false});
})

client.on('message', (topic, message, packet) => {
    console.log('Received Message: ' + message.toString() + '\\nOn topic: ' + topic)

    deviceWho = null;
    try {
        if (topic === 'testtopic') {
            var jsonData = JSON.parse(message.toString());
            if (jsonData && typeof jsonData === 'object') {

                if (jsonData.B === "02:02:17:00:01:01") {
                    deviceWho = device1Msg;
                }
                if (jsonData.B === "02:02:17:00:02:02") {
                    deviceWho = device2Msg;
                }
                console.log("deviceWho now:"+deviceWho.macAddress);

                deviceWho.header = jsonData.A;
                deviceWho.macAddress = jsonData.B;
                deviceWho.date = jsonData.D;
                deviceWho.time = jsonData.E;
                // setSensorData(data.F)
                deviceWho.setSensorData(jsonData.F);
                // deviceWho.sensorData.humidity = jsonData.F?.F2;
                // deviceWho.sensorData.fireAlarm = jsonData.F?.F3;
                // deviceWho.sensorData.pressure = jsonData.F?.F4;
                // deviceWho.sensorData.lightIntensity = jsonData.F?.F5;
                // deviceWho.sensorData.GPS = jsonData.F?.F6;
                deviceWho.footer = jsonData.I;



                // myMqttMsg.data.header = jsonData.A;
                // myMqttMsg.data.macAddress = jsonData.B;
                // myMqttMsg.data.date = jsonData.D;
                // myMqttMsg.data.time = jsonData.E;
                // myMqttMsg.data.sensorData.temperature = jsonData.F?.F1;
                // myMqttMsg.data.sensorData.humidity = jsonData.F?.F2;
                // myMqttMsg.data.sensorData.fireAlarm = jsonData.F?.F3;
                // myMqttMsg.data.sensorData.pressure = jsonData.F?.F4;
                // myMqttMsg.data.sensorData.lightIntensity = jsonData.F?.F5;
                // myMqttMsg.data.sensorData.GPS = jsonData.F?.F6;
                // myMqttMsg.data.footer = jsonData.I;

                BMapUpdate()

                console.log('Data extracted and saved to variables.');
            } else {
                console.error('Invalid JSON data received.');
            }
        }
    } catch (error) {
        console.error('Error parsing JSON data:', error);
    }


    if (topic === 'WillMsg') {
        // 使用split方法以等号为分隔符将字符串分割成键和值
        const keyValueArray = message.toString().split('=');

        // 检查是否成功分割为两部分，然后获取键和值
        if (keyValueArray.length === 2) {
            const status = keyValueArray[0];
            const device = keyValueArray[1];


            console.log('status:', status);     // 输出: Key: online
            console.log('device:', device); // 输出: Value: 1

            if (status === 'online') {
                myMqttMsg.deviceOnline = true;

            } else {
                myMqttMsg.deviceOnline = false;

            }

        } else {
            console.log('Invalid message format.');
        }

    }

})

client.on('close', () => {
    console.log(clientId + ' disconnected')
})

// client.publish(topic, message, {qos: 0, retain: false});


function tickChoice() {

    console.log("myMqttMsg.deviceChoice now:"+myMqttMsg.deviceChoice.macAddress);
    console.log("sensorData.temperature now:"+myMqttMsg.deviceChoice.sensorData.temperature);
    console.log("sensorData.GPS now:"+myMqttMsg.deviceChoice.sensorData.GPS);
    myMqttMsg.data.header = myMqttMsg.deviceChoice.header;
    myMqttMsg.data.macAddress = myMqttMsg.deviceChoice.macAddress;
    myMqttMsg.data.date = myMqttMsg.deviceChoice.date;
    myMqttMsg.data.time = myMqttMsg.deviceChoice.time;
    myMqttMsg.data.sensorData.temperature = myMqttMsg.deviceChoice.sensorData.temperature;
    myMqttMsg.data.sensorData.humidity = myMqttMsg.deviceChoice.sensorData.humidity;
    myMqttMsg.data.sensorData.fireAlarm = myMqttMsg.deviceChoice.sensorData.fireAlarm;
    myMqttMsg.data.sensorData.pressure = myMqttMsg.deviceChoice.sensorData.pressure;
    myMqttMsg.data.sensorData.lightIntensity = myMqttMsg.deviceChoice.sensorData.lightIntensity;
    myMqttMsg.data.sensorData.GPS = myMqttMsg.deviceChoice.sensorData.GPS;
    myMqttMsg.data.footer = myMqttMsg.deviceChoice.footer;

    window.setTimeout("tickChoice()", 1000);
}

tickChoice();

