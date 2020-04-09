$(document).ready(function() {
    var myChart1 = echarts.init(document.getElementById('index1'));
    myChart1.showLoading();

    var myChart2 = echarts.init(document.getElementById('index2'));
    myChart2.showLoading();

    $.ajax({
        //url: "{% url 'index' %}",
        url:"/index/",
        type: "GET",
        data: {},
        success: function (data) {
            myChart1.hideLoading();
            data = JSON.parse(data);
            myChart1.setOption({
                legend: {},
                tooltip: {},
                dataset: {
                    source: data['source']
                },
                xAxis: {type: 'category'},
                yAxis: {},
                // Declare several bar series, each will be mapped
                // to a column of dataset.source by default.
                series: [
                    {type: 'bar'},
                    {type: 'bar'},
                    {type: 'bar'},
                    {type: 'bar'}
                ]
            });
            myChart2.hideLoading();
            myChart2.setOption({
                legend: {},
                tooltip: {},
                xAxis: {
                    type: 'category',
                    data: data['districts']
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    data: data['number'],
                    type: 'line'
                }]
            });
        }
    })
});