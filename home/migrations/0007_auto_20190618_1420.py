# Generated by Django 2.2 on 2019-06-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190617_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sub_type',
            field=models.CharField(blank=True, default='None', max_length=100, null=True, verbose_name='产品二级分类'),
        ),
    ]