# Generated by Django 2.2 on 2019-05-23 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0003_auto_20190523_1026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimgs',
            options={'verbose_name_plural': '产品图集'},
        ),
        migrations.AlterField(
            model_name='productimgs',
            name='images',
            field=models.ImageField(upload_to='product_img/', verbose_name='图片地址'),
        ),
        migrations.AlterField(
            model_name='productimgs',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.Product', verbose_name='产品'),
        ),
        migrations.CreateModel(
            name='CasesImgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='cases_img/', verbose_name='图片地址')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('cases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.Cases')),
            ],
            options={
                'verbose_name_plural': '工程案例图集',
            },
        ),
    ]
