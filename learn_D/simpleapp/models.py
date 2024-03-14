from django.db import models
from django.core.validators import MinValueValidator


# Товар для нашей витрины
class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, # названия товаров не должны повторяться
    )
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]} - Price {self.price} rubley'


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class News(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='news')
    published = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'