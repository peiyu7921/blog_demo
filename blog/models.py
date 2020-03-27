from django.db import models
from django.contrib import admin
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=32, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment_num = models.IntegerField(default=0, null=False)
    introduction = models.CharField(max_length=256, null=False)
    content = models.TextField(null=False)

    def __str__(self):  # 增加该方法
        return self.title

    class Mete:
        db_table = "article"
        ordering = ('-updated_at',)


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, to_field='id', on_delete=models.CASCADE, null=False)
    content = models.TextField(null=False)

    class Mete:
        db_table = "comment"


admin.site.register(Article)
admin.site.register(Comment)