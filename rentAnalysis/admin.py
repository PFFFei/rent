from django.contrib import admin
from .models import Rent


admin.site.site_title = '二手房信息管理系统'
admin.site.site_header = '二手房信息管理系统'


class RentAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Rent, RentAdmin)
