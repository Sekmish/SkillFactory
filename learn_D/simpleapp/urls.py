from django.urls import path
from .views import ProductsList, ProductDitail, NewsList, NewsDetail, multiply, ProductCreate, ProductUpdate, ProductDelete, NewsListSearch
urlpatterns = [
    path('products/', ProductsList.as_view(), name='products_list'),
    path('products/<int:hren>', ProductDitail.as_view(), name='product_detail'),
    path('news/', NewsList.as_view()),
    path('news/<int:pk>', NewsDetail.as_view()),
    path('multiply/', multiply),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('news/search', NewsListSearch.as_view(), name='search_news'),

]
