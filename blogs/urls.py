from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # 首页
    path('', views.index, name='index'),
    # 新建博文
    path('new/', views.new_blog, name='new_blog'),
    # 编辑博文，<int:blog_id> 为路径参数
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
]