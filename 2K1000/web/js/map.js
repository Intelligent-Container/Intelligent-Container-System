
function BMapUpdate() {

// 拆分经纬度字符串
    const coordinates = myMqttMsg.data.sensorData.GPS.split('&');

    if (myMqttMsg.lng === parseFloat(coordinates[0])&&myMqttMsg.lat === parseFloat(coordinates[1]))
    {
        console.log("=======")
        return;

    }else
    {
        console.log("xxxxxxx")
        myMqttMsg.lng = parseFloat(coordinates[0]);
        myMqttMsg.lat = parseFloat(coordinates[1]);
    }

// 提取经度和纬度
//     let lng = parseFloat(coordinates[0]);
//     let lat = parseFloat(coordinates[1]);
    let lng = myMqttMsg.lng ;
    let lat = myMqttMsg.lat ;
// lng = 103.892736;//lng：是Longtitude的简写，表示经度；
// lat = 30.793023;//lat：是Latitude的简写，表示纬度；
// 30.789329,103.888352这是学校的维经度

var map = new BMapGL.Map("distribution_map");
// var point = new BMapGL.Point(116.404, 39.915);//其中116.404表示经度，39.915表示纬度
var point = new BMapGL.Point(lng, lat);
var scaleCtrl = new BMapGL.ScaleControl();  // 添加比例尺控件
map.addControl(scaleCtrl);
var zoomCtrl = new BMapGL.ZoomControl();  // 添加缩放控件
map.addControl(zoomCtrl);
var cityCtrl = new BMapGL.CityListControl();  // 添加城市列表控件
map.addControl(cityCtrl);
map.enableScrollWheelZoom(true);     //开启鼠标滚轮缩放
// 地图类型常量：
//
// 1.标准地图：BMAP_NORMAL_MAP
// 2.地球模式：BMAP_EARTH_MAP
// 3.普通卫星地图：BMAP_SATELLITE_MAP
map.setMapType(BMAP_EARTH_MAP);

map.centerAndZoom(point, 15);
// 创建图标
var myIcon = new BMapGL.Icon("mark.png", new BMapGL.Size(48, 48));
// 生成标记点
marker = new BMapGL.Marker(new BMapGL.Point(lng, lat), {
    icon: myIcon
});
map.addOverlay(marker);

// 生成文本标注
// var point = new BMapGL.Point(116.404, 39.915);
var content = '经度：' + lng + '  ' + '纬度：' + lat;
var label = new BMapGL.Label(content, {       // 创建文本标注
    position: point,
    offset: new BMapGL.Size(10, 20)
})
map.addOverlay(label);                        // 将标注添加到地图中
label.setStyle({                              // 设置label的样式
    color: 'rgba(0,0,0,1)',
    // background: 'rgba(0,0,0,0)',
    borderRadius: '5px',
    borderColor: '#ccc',
    padding: '10px',
    fontSize: '.9vw',
    lineHeight: '3.5vh',
    fontFamily: '微软雅黑'
})
}

BMapUpdate()