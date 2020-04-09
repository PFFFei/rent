$(document).ready(function() {
    var myChart1 = echarts.init(document.getElementById('district1'));
    myChart1.showLoading();
    $.ajax({
        url:"/district/",
        type: "GET",
        data: {},
        success: function (data) {
            myChart1.hideLoading();
            data = JSON.parse(data);
            myChart1.setOption({
                series : [
                    {
                        name: '房屋结构',
                        type: 'pie',
                        radius: '55%',
                        data:data
                    }
                ]
            })
        }
    })
});