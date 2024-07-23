# Generated by Django 5.0.6 on 2024-07-23 14:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_created_at_remove_blog_preview_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='product/image', verbose_name='Изображение (превью)'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=True, help_text='Опубликовать блог', verbose_name='Опубликовано'),
        ),
    ]