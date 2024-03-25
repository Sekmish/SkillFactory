from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from django.forms.widgets import SelectDateWidget
from .models import Product, Category, News
from datetime import datetime, timedelta

class ProductFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='category',
        to_field_name='name',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Все'
        )

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'quantity': ['gt'],
            'price': ['lt', 'gt'],
        }


class CustomSelectDateWidget(SelectDateWidget):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        if value is None:
            label = ('День, Месяц, Год')
        return super().create_option(name, value, label, selected, index, subindex, attrs)


class NewsFilter(FilterSet):
    current_year = datetime.now().year
    years_range = range(2020, current_year + 1)

    published_after = DateFilter(
        field_name='published',
        lookup_expr='gt',
        widget=SelectDateWidget(years=years_range),
        label='Искать с '
    )

    published_before = DateFilter(
        field_name='published',
        method='filter_published_before',
        widget=SelectDateWidget(years=years_range),
        label='Искать до '
    )

    category = ModelChoiceFilter(
        field_name='category__name',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Все новости'
    )

    def filter_published_before(self, queryset, name, value):
        value = value + timedelta(days=1)  # Добавляем один день к выбранной дате
        return queryset.filter(**{f'{name}__lt': value}).order_by('published')


    class Meta:
        model = News
        fields = {
            'title': ['icontains'],
            'category': ['exact'],
        }
