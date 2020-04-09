## 成都⼆⼿房爬⾍及可视化

**开发环境**：**Scrapy**、**Django2.x**

**项⽬描述**：该项⽬使⽤ **Scrapy** 框架爬取链家成都地区⼆⼿房数据，通过 **Django** 框架写⼊数据库并使⽤ **ECharts** 将分析后的数据可视化展⽰到⽹⻚。

#### 教程

- 创建Django工程

```
djagno-admin startproject rent
```
- 进入rent目录并创建Django项目

```
cd rent

python manage.py startapp rentAnalysis
```
- 创建Scrapy工程
```
scrapy startproject rentSpider
```
- 进入rentSpider目录并创建爬虫文件
```
cd rentSpider

scrapy genspider house(spider_name) cd.lianjia.com(spider_url)
```
- 在Scrapy工程中配置Django

```
# rentSpider/settings.py

import os
import sys
import django
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rent.settings')  # Django Project Name
django.setup()
```
- 启动Scrapy

```
scrapy crawl house(spider_name)
```
- 启动Django

```
python manage.py runserver
```

```
admin: rent
password: rent1234
```
