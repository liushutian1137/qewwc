from django.urls import path
from . import views

app_name = 'chpa'  # 这句是必须的，和之后所有的URL语句有关
urlpatterns = [
    path(r'index', views.index, name='index'),
]