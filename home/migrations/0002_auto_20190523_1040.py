# Generated by Django 2.2 on 2019-05-23 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cases',
            options={'verbose_name_plural': '      工程案例'},
        ),
        migrations.AlterModelOptions(
            name='casesimgs',
            options={'verbose_name_plural': '     工程案例图集'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': '   新闻中心'},
        ),
        migrations.AlterModelOptions(
            name='newstype',
            options={'verbose_name_plural': '    新闻分类'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '         产品'},
        ),
        migrations.AlterModelOptions(
            name='productimgs',
            options={'verbose_name_plural': '        产品图集'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name_plural': '          产品分类'},
        ),
        migrations.AlterModelOptions(
            name='solution',
            options={'verbose_name_plural': '      净化方案'},
        ),
        migrations.AlterModelOptions(
            name='solutiontype',
            options={'verbose_name_plural': '       解决方案分类'},
        ),
        migrations.AlterField(
            model_name='newstype',
            name='title',
            field=models.SmallIntegerField(choices=[(1, '顺尚动态'), (2, '行业资讯'), (3, '净化技术')], max_length=30, verbose_name='新闻分类'),
        ),
    ]
