from django import forms
from django.core.exceptions import ValidationError

from .models import Product

class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=20)
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'quantity',
            'category',
            'price'
        ]


    def clean(self): #используется если надо проверить несколько полей
        cleaned_data = super().clean()

        description = cleaned_data.get('description')
        # if description is not None and len(description) < 20:
        #     raise ValidationError({'description': 'Описание не может быть менее 20 символов.'})

        name = cleaned_data.get('name')
        if name == description:
            raise ValidationError('Описание не должно быть идентично названию.')

        return cleaned_data


    def clean_name(self): # Если требуется проверить одно поле сложным образом, создайте для этого метод clean_fieldname.
        name = self.cleaned_data['name']
        if name[0].islower():
            raise ValidationError('Название должно начинаться с заглавной буквы.')
        return name