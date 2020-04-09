from django.db import models


class Rent(models.Model):
    district = models.CharField(max_length=20, verbose_name='区域')
    title = models.CharField(max_length=256, verbose_name='标题')
    bedroom = models.CharField(max_length=20, verbose_name='房厅')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=10, verbose_name='装修')
    total_price = models.FloatField(verbose_name='总价(万元)')
    unit_price = models.IntegerField(verbose_name='单价(元/平方米)')

    add_date = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    mod_date = models.DateTimeField(auto_now=True, verbose_name="修改日期")

    class Meta:
        verbose_name = '二手房'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}-{}".format(self.title, self.total_price)


