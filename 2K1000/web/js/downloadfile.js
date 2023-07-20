
  // 当按钮点击时执行的函数
  function downloadExcelFile() {
    // 获取当前日期
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0'); // 月份从0开始，需要+1并补0
    const day = String(today.getDate()).padStart(2, '0'); // 补0以保证两位数的日期

    // 构建文件名，格式为“年_月_日.xlsx”
    const fileName = `D${year}_${month}_${day}.xls`;

    // 创建一个虚拟a标签，并设置其属性
    const link = document.createElement('a');
    link.href = fileName;
    link.download = fileName;

    // 添加该虚拟a标签到文档中，并模拟点击
    document.body.appendChild(link);
    link.click();

    // 移除该虚拟a标签
    document.body.removeChild(link);
  }
