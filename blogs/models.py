from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """博客文章模型"""
    title = models.CharField(max_length=200, verbose_name="标题")
    text = models.TextField(verbose_name="内容")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    
    # 阶段2新增：关联用户模型，on_delete=CASCADE表示用户删除后其博文也删除
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")

    class Meta:
        verbose_name_plural = "博文列表"

    def __str__(self):
        """返回模型的字符串表示"""
        return self.title