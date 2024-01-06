from django.views.generic import ListView, DetailView

from news.models import News


class NewsListView(ListView):
    queryset = News.published.all()
    template_name = 'news/news-list.html'
    context_object_name = 'articles'


class NewsDetailView(DetailView):
    queryset = News.published.all()
    template_name = 'news/news-detail.html'
    context_object_name = 'article'
