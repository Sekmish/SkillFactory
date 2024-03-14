from datetime import datetime
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Product, News

class ProductsList(ListView):
    model = Product
    ordering = 'name'
    # queryset = Product.objects.filter(
    #     price__gt=20
    # ).order_by('-name')
    template_name = 'products.html'
    context_object_name = 'products'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_sale'] = 'Распродажа в субботу!'
        return context


class ProductDitail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'hren'


class NewsList(ListView):
    model = News
    ordering = '-pk'
    template_name = 'news.html'
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'
