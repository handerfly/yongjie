# Generated by Django 2.2 on 2019-06-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20190603_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='cover',
            field=models.ImageField(default='cases_cover/cases_cover.jpg', help_text='建议图片大小：360*258像素', upload_to='cases_cover/', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='news',
            name='cover',
            field=models.ImageField(default='news_cover/news_cover.jpg', help_text='建议图片大小：360*258像素', upload_to='news_cover/', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cover',
            field=models.ImageField(default='products_cover/products_cover.jpg', help_text='建议图片大小：360*258像素', upload_to='news_cover/', verbose_name='封面图片'),
        ),
    ]
