# Generated by Django 2.2 on 2019-05-24 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='is_deleted',
            field=models.BooleanField(default=True, help_text='勾选表示可用', verbose_name='状态'),
        ),
    ]