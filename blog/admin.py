from django.contrib import admin
from .models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "views",
        "is_published",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "content")
    list_filter = ("is_published", "created_at")
    ordering = ("-created_at",)
    list_per_page = 20


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ('name',)
    ordering = ("id",)