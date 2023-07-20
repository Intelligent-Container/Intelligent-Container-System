// 模拟设备在线状态，true表示在线，false表示离线
function tickStatus2() {
// 获取显示设备状态的div元素2
var fireStatusElement = document.getElementById("fireStatus");
var fireIconElement = document.getElementById("fireIcon");


// 根据设备在线状态设置显示样式和文本内容

if (myMqttMsg.data.sensorData.fireAlarm==='1') {
    fireStatusElement.innerText = "有火";
    fireStatusElement.style.color = "red";
    fireIconElement.src = "images/fire.png"; // 添加有火图标的图片路径
    fireIconElement.style.width = "100px"; // 设置宽度为100像素
    fireIconElement.style.height = "100px"; // 设置高度为100像素
} else {
    fireStatusElement.innerText = "无火";
    fireStatusElement.style.color = "green";
    fireIconElement.src = "images/water-drop.png"; // 添加有火图标的图片路径
    fireIconElement.style.width = "100px"; // 设置宽度为100像素
    fireIconElement.style.height = "100px"; // 设置高度为100像素
}
    // console.log("fire"+myMqttMsg.data.sensorData.fireAlarm);
    window.setTimeout("tickStatus2()", 1000);
}
document.addEventListener("DOMContentLoaded", function() {

tickStatus2();

});