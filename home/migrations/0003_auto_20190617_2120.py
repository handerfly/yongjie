# Generated by Django 2.2 on 2019-06-17 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190617_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Category', verbose_name='产品大类'),
        ),
    ]
