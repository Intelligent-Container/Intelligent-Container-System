$(function() {
  //湿度
    var dom = document.getElementById("containersd");
    var myChart = echarts.init(dom);
    var app = {};
    option = null;
    option =  {
  series: [
    {
      type: 'gauge',
      startAngle: 200,
      endAngle: -20,
      center: ['50%', '60%'],
      radius: '90%',
      min: 0,
      max: 1,
      splitNumber: 8,
      axisLine: {
        lineStyle: {
          width: 10,
          color: [
            [0.25, '#a7535a'],
            [0.5, '#8e804b'],
            [0.75, '#0f95b0'],
            [1, '#428675']
          ]
        }
      },
      pointer: {
        icon: 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
        length: '12%',
        width: 20,
        offsetCenter: [0, '-50%'],
        itemStyle: {
          color: 'inherit'
        }
      },
      axisTick: {
        length: 12,

        lineStyle: {
          color: 'inherit',
          width: 2
        }
      },
      splitLine: {
        length: 20,

        lineStyle: {
          // color: 'inherit',
           color: '#f3f3f3',
          width: 3
        }
      },
      axisLabel: {
        color: '#999999',
        fontSize: 18,
        distance: -65,
        rotate: 'tangential',
        formatter: function (value) {
          if (value === 1) {
            return '100%';
          } else if (value === 0.75) {
            return '75%';
          } else if (value === 0.50) {
            return '50%';
          } else if (value === 0.25) {
            return '25%';
          }else if (value === 0.0) {
            return '0%';
          }
          return '';
        }
      },
      title: {
        offsetCenter: [0, '-10%'],
        fontSize: 20
      },
      detail: {//中心变化数值的属性
        fontSize: 30,
        offsetCenter: [0, '-0%'],
        valueAnimation: true,
        formatter: function (value) {
          return Math.round(value * 100) + ' %rh';
        },
        color: 'inherit'
      },
      data: [
        {
          value: 0.7,
          name: ' '
        }
      ]
    }
  ]
};


setInterval(function () {
const random = +(Math.random() * 100);
    myChart.setOption({
    series: [
      {
        data: [
          {
            value: myMqttMsg.data.sensorData.humidity/100
            // value: random/100
          }
        ]
      }
    ]
  });
}, 2000);
    ;
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
});