from django.urls import path
from .views import home, bedroom, index, district

app_name = 'rentAnalysis'

urlpatterns = [
    path('', home, name='home'),
    path('bedroom/', bedroom, name='bedroom'),
    path('index/', index, name='index'),
    path('district/', district, name='district'),
]