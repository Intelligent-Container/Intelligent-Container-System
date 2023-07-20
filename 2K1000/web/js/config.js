/*
json串格式：
var data = {
    "A": "start",
    "B": "02:02:17:00:01:01",
    "D": ["2023", "5", "14"],
    "E": ["10", "35", "57"],
    "F": {"F1": "26.89",
        "F2": "60",
        "F3": "0",
        "F4": "94088.48",
        "F5": "267.94"},
    "I": "end"
}
变量名对应：
A: header
B: macAddress
C: batteryLevel
D: date
E: time
F: sensorData
    F1: temperature
    F2: humidity
    F3: fireAlarm
    F4: pressure
    F5: lightIntensity
I: footer
*/

//创建命名空间对象
var myMqttMsg = {};
//在命名空间对象中定义变量（后续还是需要定义初始化的值）
myMqttMsg.lng = 30.4738067;
myMqttMsg.lat = 103.5302522;
myMqttMsg.deviceOnline = true;


myMqttMsg.data = {
    A: "start",
    B: "02:02:17:00:01:01",
    D: ["2023", "5", "14"],
    E: ["10", "35", "57"],
    F: {
        F1: "26.89",
        F2: "60",
        F3: "0",
        F4: "94088.48",
        F5: "267.94",
        F6: "103.5302522&30.4738067"
    },
    I: "end",

//设置别名和原始变量之间的同步
    get header() {
        return this.A;
    },
    set header(value) {
        this.A = value;
    },

    get macAddress() {
        return this.B;
    },
    set macAddress(value) {
        this.B = value;
    },

    get date() {
        return this.D;
    },
    set date(value) {
        this.D = value;
    },

    get time() {
        return this.E;
    },
    set time(value) {
        this.E = value;
    },

    get sensorData() {
        return {
            get temperature() {
                return myMqttMsg.data.F.F1;
            },
            set temperature(value) {
                myMqttMsg.data.F.F1 = value;
            },

            get humidity() {
                return myMqttMsg.data.F.F2;
            },
            set humidity(value) {
                myMqttMsg.data.F.F2 = value;
            },

            get fireAlarm() {
                return myMqttMsg.data.F.F3;
            },
            set fireAlarm(value) {
                myMqttMsg.data.F.F3 = value;
            },

            get pressure() {
                return myMqttMsg.data.F.F4;
            },
            set pressure(value) {
                myMqttMsg.data.F.F4 = value;
            },

            get lightIntensity() {
                return myMqttMsg.data.F.F5;
            },
            set lightIntensity(value) {
                myMqttMsg.data.F.F5 = value;
            },

            get GPS() {
                return myMqttMsg.data.F.F6;
            },
            set GPS(value) {
                myMqttMsg.data.F.F6 = value;
            }
        };
    },
    get footer() {
        return this.I;
    },
    set footer(value) {
        this.I = value;
    }
};


class deviceMsg {
    constructor() {
        // 定义对应的英文变量
        this.header = "start";
        this.macAddress = "02:02:17:00:01:01";
        this.date = ["2023", "5", "14"];
        this.time = ["10", "35", "57"];
        this.sensorData = {
            temperature: "26.89",
            humidity: "60",
            fireAlarm: "0",
            pressure: "94",
            lightIntensity: "429",
            GPS: "103.5302522&30.4738067"
        };
        this.footer = "end";
    }

    // 方法用于设置sensorData字段的值
    setSensorData(sensorData) {
        this.sensorData.temperature = sensorData.F1;
        this.sensorData.humidity = sensorData.F2;
        this.sensorData.fireAlarm = sensorData.F3;
        this.sensorData.pressure = sensorData.F4;
        this.sensorData.lightIntensity = sensorData.F5;
        this.sensorData.GPS = sensorData.F6;
    }

    // 方法用于获取sensorData字段的值
    getSensorData() {
        return this.sensorData;
    }
}

// 根据提供的JSON数据创建实例化对象
// const data = {
//   "A": "start",
//   "B": "02:02:17:00:01:01",
//   "D": ["2023", "5", "14"],
//   "E": ["10", "35", "57"],
//   "F": {
//     "F1": "26.89",
//     "F2": "60",
//     "F3": "0",
//     "F4": "94088.48",
//     "F5": "267.94"
//   },
//   "I": "end"
// };

const device1Msg = new deviceMsg();
const device2Msg = new deviceMsg();

myMqttMsg.deviceChoice = device1Msg;

// dataObject.date = data.D;
// dataObject.time = data.E;
// dataObject.setSensorData(data.F);

// 示例：通过实例化对象调用不同对象的相同的全局变量
// console.log(dataObject.header); // 输出 "start"
// console.log(dataObject.macAddress); // 输出 "02:02:17:00:01:01"
// console.log(dataObject.date); // 输出 ["2023", "5", "14"]
// console.log(dataObject.time); // 输出 ["10", "35", "57"]
// console.log(dataObject.getSensorData()); // 输出sensorData对象，包含temperature、humidity、fireAlarm、pressure和lightIntensity字段
// console.log(dataObject.footer); // 输出 "end"


function deviceChoice(deviceNum) {
    var deviceStatusElement1 = document.getElementById("device1");
    var deviceStatusElement2 = document.getElementById("device2");
    if (deviceNum === 1) {
        myMqttMsg.deviceChoice = device1Msg;
        console.log("device now:" + deviceNum);

// 根据设备在线状态设置显示样式和文本内容
//         deviceStatusElement.innerText = "集装箱1";
        deviceStatusElement1.style.color = "green";
        deviceStatusElement2.style.color = "#00f6ff";
    }

        if (deviceNum === 2) {
            myMqttMsg.deviceChoice = device2Msg;

            console.log("device now:" + deviceNum);
            myMqttMsg.deviceOnline = true;

// 根据设备在线状态设置显示样式和文本内容
//         deviceStatusElement.innerText = "集装箱2";
        deviceStatusElement1.style.color = "#00f6ff";
        deviceStatusElement2.style.color = "green";

        }
    }