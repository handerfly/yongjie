# Generated by Django 2.2 on 2019-06-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_solutiontype_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cover',
            field=models.ImageField(default='products_cover/products_cover.jpg', help_text='建议图片大小：360*258像素', upload_to='products_cover/', verbose_name='封面图片'),
        ),
    ]
