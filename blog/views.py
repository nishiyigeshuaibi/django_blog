from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Article

def index(request):
    articles = Article.objects.filter(is_published=True)

    context = {
        "blog_name": "我的技术博客",
        "articles": articles,
    }

    return render(request, "blog/index.html", context)


def detail(request, article_id):
    article = get_object_or_404(
        Article,
        id=article_id,
        is_published=True
    )

    context = {
        "article": article,
    }

    return render(request, "blog/detail.html", context)
