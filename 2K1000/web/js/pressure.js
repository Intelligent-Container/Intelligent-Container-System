$(function() {
  //大气压强
    var dom = document.getElementById("containerqy");
    var myChart = echarts.init(dom);
    var app = {};
    option = null;
    // Generate data
    // var category = [];
    // var dottedBase = +new Date();
    // dottedBase-=3600 * 24 * 1000*20;
    // var lineData = [];
    // var barData = [];

    // for (var i = 0; i < 20; i++) {
    //     var date = new Date(dottedBase += 3600 * 24 * 1000);
    //     category.push([
    //         date.getFullYear(),
    //         date.getMonth() + 1,
    //         date.getDate()
    //     ].join('-'));
    //     var b = vm.msgCnt[i].msg;
    //     var d = vm.msgCnt[i].alm;
    //     barData.push(b)
    //     lineData.push(d + b);
    // }


    // option
    option = {
  series: [
    {
      type: 'gauge',
      min: 0,
      max: 100,
      splitNumber: 10,
      radius: '70%',//圈大小尺寸
      axisLine: {//外层弧线
        lineStyle: {
          color: [[1, '#1661ab']],
          width: 3
        }
      },
      splitLine: {//外层长线刻度
        distance: -18,
        length: 18,
        lineStyle: {
          color: '#1661ab'
        }
      },
      axisTick: {//外层小刻度
        distance: -12,
        length: 10,
        lineStyle: {
          color: '#1661ab'
        }
      },
      axisLabel: {//外层数值
        distance: -40,
        color: '#1661ab',
        fontSize: 18
      },
      anchor: {//中心白圈
        show: true,
        size: 20,
        itemStyle: {
          borderColor: '#5e7987',
          borderWidth: 2
        }
      },
      pointer: {//指针属性
        offsetCenter: [0, '10%'],
        icon: 'path://M2090.36389,615.30999 L2090.36389,615.30999 C2091.48372,615.30999 2092.40383,616.194028 2092.44859,617.312956 L2096.90698,728.755929 C2097.05155,732.369577 2094.2393,735.416212 2090.62566,735.56078 C2090.53845,735.564269 2090.45117,735.566014 2090.36389,735.566014 L2090.36389,735.566014 C2086.74736,735.566014 2083.81557,732.63423 2083.81557,729.017692 C2083.81557,728.930412 2083.81732,728.84314 2083.82081,728.755929 L2088.2792,617.312956 C2088.32396,616.194028 2089.24407,615.30999 2090.36389,615.30999 Z',
        length: '115%',
        itemStyle: {
          color: '#000'
        }
      },
      detail: {//变化刻度值
        fontSize: 24,
        color: '#63bbd0',
        valueAnimation: true,
        precision: 1
      },
      title: {//PLP
        fontSize: 15,
        color: '#ff7070',
        offsetCenter: [0, '-40%']

      },
      data: [
        {
          value: 58.46,
          name: 'kpa'
        }
      ]
    },
    {
      type: 'gauge',
      min: 0,
      max: 60,
      splitNumber: 6,
      radius: '65%',//圈大小尺寸
      axisLine: {//内层弧线
        lineStyle: {
          color: [[1, '#5e7987']],
          width: 4
        }
      },
      splitLine: {//内层长线刻度
        distance: -3,
        length: 18,
        lineStyle: {
          color: '#5e7987'
        }
      },
      axisTick: {//内层小刻度
        distance: 0,
        length: 10,
        lineStyle: {
          color: '#5e7987'
        }
      },
      axisLabel: {//内层数值
        distance: 10,
        fontSize: 18,
        color: '#fff'
      },
      pointer: {
        show: false
      },
      title: {
        show: false
      },
      anchor: {
        show: true,
        size: 14,
        itemStyle: {
          color: '#000'
        }
      }
    }
  ]
};
setInterval(function () {
  myChart.setOption({
    series: [
      {
        type: 'gauge',
        data: [
          {
            value: myMqttMsg.data.sensorData.pressure,
            name: 'kpa'
          }
        ]
      }
    ]
  });
}, 2000);;
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
})