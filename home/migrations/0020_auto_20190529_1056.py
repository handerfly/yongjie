# Generated by Django 2.2 on 2019-05-29 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20190524_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='cover',
            field=models.ImageField(default='cases_cover/newscover.jpg', help_text='建议图片大小：360*258像素', upload_to='cases_cover/', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='news',
            name='cover',
            field=models.ImageField(default='news_cover/newscover.jpg', help_text='建议图片大小：360*258像素', upload_to='news_cover/', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cover',
            field=models.ImageField(default='products_cover/newscover.jpg', help_text='建议图片大小：360*258像素', upload_to='news_cover/', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='cover',
            field=models.ImageField(help_text='建议图片大小：360*258像素', upload_to='solution_cover/', verbose_name='封面图片'),
        ),
    ]