from django.db import models


class Category(models.Model):
    title = models.CharField(
        verbose_name="分类名称",
        max_length=50,
        unique=True,
    )
    created_at = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="更新时间",
        auto_now=True,
    )

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = "文章分类"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(
        verbose_name="文章标题",
        max_length=200,
    )
    content = models.TextField(
        verbose_name="文章正文",
    )
    views = models.PositiveIntegerField(
        verbose_name="阅读次数",
        default=0,
    )
    is_published = models.BooleanField(
        verbose_name="是否发布",
        default=False,
    )
    created_at = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="更新时间",
        auto_now=True,
    )

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def __str__(self):
        return self.title