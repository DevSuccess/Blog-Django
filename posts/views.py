from django.shortcuts import render
from django.views import generic

from . import models


# Create your views here.
class ArticleList(generic.ListView):
    queryset = models.Article.objects.filter(status=1)
    template_name = 'posts/index.html'


class ArticleDetail(generic.DetailView):
    model = models.Article
    template_name = 'posts/detail.html'
