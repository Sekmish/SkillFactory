from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ProductForm
from .models import Product, News
from django.http import HttpResponse
from .filters import ProductFilter, NewsFilter
from django.contrib.auth.mixins import LoginRequiredMixin

def multiply(request):
    number = request.GET.get('number')
    multiplier = request.GET.get('multiplier')
    try:
        result = int(number) * int(multiplier)
        html = f'<html><body>{number}*{multiplier}={result}</body></html>'
    except (ValueError, TypeError):
        html = f'<html><body>Invalid input.</body><html>'
    return HttpResponse(html)

class ProductsList(ListView):
    model = Product
    ordering = 'name'
    # queryset = Product.objects.filter(
    #     price__gt=20
    # ).order_by('-name')
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_sale'] = 'Распродажа в субботу!'
        context['filterset'] = self.filterset
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
    paginate_by = 10

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = NewsFilter(self.request.GET, queryset)
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['total_news_count'] = self.filterset.qs.count()
    #     return context

class NewsListSearch(ListView):
    model = News
    ordering = '-pk'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['total_news_count'] = self.filterset.qs.count()
        return context

class NewsDetail(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'


class ProductCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('products_list')



# def create_product(request):
#     form = ProductForm()
#
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('products_list')
#
#     return render(request, 'flatpages/product_edit.html', {'form': form})
