# Generated by Django 5.0.2 on 2024-03-12 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0002_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='discription',
            new_name='description',
        ),
    ]
