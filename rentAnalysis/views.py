from django.shortcuts import render
from .models import Rent
from django.db.models import Avg, Max, Min, Sum
from django.http import HttpResponse
import json

'''
    数据已进行预处理如下：
    for each in Rent.objects.all():
        if each.district not in [' 简装 ', ' 毛坯 ', ' 精装 ', ' 其他 ']:
            each.district = ' 其他 '
            each.save()
'''


def home(request):
    return render(request, 'index.html')


def bedroom(request):
    return render(request, 'district.html')


def index(request):
    districts = ['简阳', '新津', '彭州', '龙泉驿', '天府新区南区', '青白江', '温江', '高新西', '金牛', '武侯', '天府新区', '高新', '成华', '双流', '新都', '郫都', '都江堰', '金堂', '锦江', '大邑', '崇州', '青羊']
    decorations = [' 简装 ', ' 毛坯 ', ' 精装 ', ' 其他 ']
    source = [['decoration', '简装', '毛坯', '精装', '其他']]
    number = []
    # # 每个区域 装修类型 平均单价
    for district in districts:
        temp = [district]
        rent = Rent.objects.filter(district=district)
        number.append(rent.count())
        for decoration in decorations:
            unit_average = rent.filter(decoration=decoration).aggregate(Avg('unit_price'))
            temp.append(int(unit_average['unit_price__avg']))
        source.append(temp)
    return HttpResponse(json.dumps({'source': source, 'districts': districts, 'number': number}))


def district(request):
    temp = ['3室2厅 ', '2室2厅 ', '3室1厅 ', '4室2厅 ', '1室1厅 ', '5室2厅 ', '2室1厅 ', '6室2厅 ', '4室3厅 ', '5室1厅 ', '6室3厅 ', '2室0厅', '4室1厅 ', '车位 ', '1室0厅 ', '1室2厅 ', '5室3厅 ', '7室2厅 ', '3室3厅 ', '9室2厅 ', '3室0厅 ', '6室1厅 ', '7室1厅 ', '6室4厅', '4室4厅 ', '7室4厅 ', '0室0厅 ', '7室3厅 ', '8室2厅 ', '5室4厅 ', '2室3厅 ', '5室0厅 ', '6室5厅 ', '5室5厅 ', '7室5厅 ', '8室4厅 ', '8室3厅 ', '0室1厅 ', '8室8厅 ', '18室3厅 ', '12室3厅 ', '9室4厅 ', '9室6厅 ', '4室0厅 ', '3室4厅 ', '13室4厅 ']
    data = []
    rent = Rent.objects.filter(district='锦江')
    for each in temp:
        data.append({'value': rent.filter(bedroom=each).count(), 'name': each})

    return HttpResponse(json.dumps(data))