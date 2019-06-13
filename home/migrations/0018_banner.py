# Generated by Django 2.2 on 2019-05-24 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_delete_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='建议图片大小：1920*680像素', upload_to='banner/', verbose_name='图片')),
                ('url', models.CharField(max_length=150, verbose_name='图片链接地址')),
                ('open', models.CharField(choices=[('_self', '当前窗口'), ('_blank', '新窗口')], default='当前窗口', max_length=20, verbose_name='链接打开方式')),
                ('order', models.SmallIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default='0', help_text='数值越小排序越前', verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=True, help_text='勾选表示不可用', verbose_name='状态')),
            ],
            options={
                'verbose_name_plural': '轮番图片',
            },
        ),
    ]
