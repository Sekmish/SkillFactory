from django.urls import path
from .views import ProductsList, ProductDitail, NewsList, NewsDetail
urlpatterns = [
    path('products/', ProductsList.as_view()),
    path('products/<int:hren>', ProductDitail.as_view()),
    path('news/', NewsList.as_view()),
    path('news/<int:pk>', NewsDetail.as_view()),

]