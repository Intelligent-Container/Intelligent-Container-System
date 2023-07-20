// 模拟设备在线状态，true表示在线，false表示离线
function tickStatus() {
    var deviceStatusElement = document.getElementById("deviceStatus");
    var deviceIconElement = document.getElementById("deviceIcon");
// 根据设备在线状态设置显示样式和文本内容
    if (myMqttMsg.deviceOnline) {
        deviceStatusElement.innerText = "设备在线";
        deviceIconElement.src = "images/containers.png"; // 添加有火图标的图片路径
        deviceIconElement.style.width = "100px"; // 设置宽度为100像素
        deviceIconElement.style.height = "100px"; // 设置高度为100像素
        // deviceStatusElement.classList.add("on");
        deviceStatusElement.style.color = "green";
    } else {
        deviceStatusElement.innerText = "设备离线";
        deviceIconElement.src = "images/disconnected.png"; // 添加有火图标的图片路径
        deviceIconElement.style.width = "100px"; // 设置宽度为100像素
        deviceIconElement.style.height = "100px"; // 设置高度为100像素
        // deviceStatusElement.classList.add("off");
        deviceStatusElement.style.color = "red";
    }

    window.setTimeout("tickStatus()", 1000);
}
document.addEventListener("DOMContentLoaded", function() {

tickStatus();

});