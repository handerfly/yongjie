# Generated by Django 2.2 on 2019-05-24 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_product_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='cover',
            field=models.ImageField(default='cases_cover/newscover.jpg', help_text='（360*258）像素', upload_to='cases_cover/', verbose_name='封面图片'),
        ),
    ]