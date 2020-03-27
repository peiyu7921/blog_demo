from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Article, Comment
# Create your views here.


def index(request):
    articles = Article.objects.values('id', 'title', 'introduction', 'comment_num')
    return render(request,'index.html', {'articles': articles})


def article(request, id):
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(article=id).order_by('-created_at')
    return render(request, 'article.html', {'article': article, 'comments': comments})

def commitComment(request):
    try:
        id = request.POST.get('id')
        content = request.POST.get('content')
        # 自动转换
        article = Article.objects.get(id = id)
        if len(content) == 0:
            raise KeyError
    except BaseException as e:
        return e
    Comment.objects.create(content = content, article = article)
    article.comment_num += 1
    article.save()
    return HttpResponseRedirect('/blog/article/' + id)

