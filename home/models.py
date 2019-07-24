from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.shortcuts import reverse
from django.conf import settings

# 关于我们
class About(models.Model):
    TYPE_CHOICE = (
        (1, '公司简介'),
        (2, '文化理念'),
        (3, '联系我们'),
    )
    TYPE_DIC = {1:'公司简介', 2:'文化理念',3:'联系我们'}

    title = models.SmallIntegerField("标题", choices=TYPE_CHOICE)
    content = RichTextUploadingField("内容",config_name='my_config')

    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return "%s"%str(self.TYPE_DIC[self.title])

    class Meta:
        verbose_name_plural = "关于我们"

# 荣誉资质
class Honer(models.Model):
    title = models.CharField("标题", max_length=30)
    images = models.ImageField("图片地址", upload_to='honer_img/')

    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = " 荣誉资质"

# 售后服务
class Service(models.Model):
    content = RichTextUploadingField("内容", config_name='my_config')

    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = " 售后服务"

# 新闻分类
class NewsType(models.Model):
    TYPE_CHOICE = (
        (1, '顺尚动态'),
        (2, '行业资讯'),
        (3, '净化技术'),
    )
    TYPE_DIC = {1: '顺尚动态', 2: '行业资讯', 3: '净化技术'}
    title = models.SmallIntegerField("新闻分类", choices=TYPE_CHOICE)

    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return "%s"%str(self.TYPE_DIC[self.title])

    class Meta:
        verbose_name_plural = "    新闻分类"

# 新闻内容
class News(models.Model):
    title = models.CharField("标题",max_length=30, )
    type = models.ForeignKey(NewsType, on_delete=models.CASCADE, verbose_name="新闻分类")
    cover = models.ImageField("封面图片",
                              upload_to='news_cover/',
                              help_text="建议图片大小：360*258像素",
                              default="news_cover/news_cover.jpg")
    content = RichTextUploadingField("内容", config_name='my_config')
    author = models.CharField("作者",max_length=30, )
    viewed = models.IntegerField(default=0)

    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "   新闻中心"

    def show_content(self):
        if len(self.content)>100:
            return '{}...'.format(self.content[0:100])
        else:
            return self.content
    show_content.allow_tags = True



class Category(models.Model):
    title = models.CharField("产品大类",max_length=100)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "           产品大类"

# 产品分类
class ProductType(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name="产品大类")
    title = models.CharField("产品分类", max_length=20)
    order = models.SmallIntegerField("排序", default='0',help_text="数值越小排序越前")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "          产品分类"

# 产品
class Product(models.Model):
    title = models.CharField("产品标题", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="产品大类")
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name="产品分类")
    sub_type = models.CharField("产品二级分类", max_length=100,default='None',null=True,blank=True)
    cover = models.ImageField("封面图片", upload_to='products_cover/', help_text="建议图片大小：360*258像素",
                              default="products_cover/products_cover.jpg")
    detail = RichTextUploadingField("产品详情",config_name='my_config')

    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "         产品"

    def show_detail(self):
        if len(self.detail)>100:
            return '{}...'.format(self.detail[0:100])
        else:
            return self.detail
    show_detail.allow_tags = True


# 产品图集
class ProductImgs(models.Model):
    images = models.ImageField("图片地址", upload_to='product_img/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="产品")

    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "        产品图集"

# 解决方案分类
class SolutionType(models.Model):
    title = models.CharField("解决方案分类", max_length=30)
    order = models.SmallIntegerField("排序", default='0',help_text="数值越小排序越前")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "       解决方案分类"

# 解决方案
class Solution(models.Model):
    title = models.CharField("净化方案标题", max_length=100)
    order = models.SmallIntegerField("排序", default='0', help_text="数值越小排序越前")
    type = models.ForeignKey(SolutionType, on_delete=models.CASCADE, verbose_name="解决方案")
    cover = models.ImageField("封面图片", upload_to='solution_cover/', help_text="建议图片大小：360*258像素")
    detail = RichTextUploadingField("净化方案详情", config_name='my_config')

    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "      净化方案"

    def show_detail(self):
        if len(self.detail)>100:
            return '{}...'.format(self.detail[0:100])
        else:
            return self.detail
    show_detail.allow_tags = True

# 工程案例
class Cases(models.Model):
    TYPE_CHOICE = (
        (1,'三十万级净化工程'),
        (2,'十万级净化工程'),
        (3,'万级净化工程'),
        (4,'千级净化工程'),
        (5,'百级净化工程')
    )
    title = models.CharField("标题", max_length=100)
    solution = models.ForeignKey(SolutionType, on_delete=models.CASCADE, verbose_name="解决方案")

    type = models.SmallIntegerField("分类", choices=TYPE_CHOICE)
    cover = models.ImageField("封面图片", upload_to='cases_cover/', help_text="建议图片大小：360*258像素",
                              default="cases_cover/cases_cover.jpg")
    detail = RichTextUploadingField("工程案例介绍",config_name='my_config')

    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "      工程案例"

# 工程案例图集
class CasesImgs(models.Model):
    images = models.ImageField("图片地址", upload_to='cases_img/')
    cases = models.ForeignKey(Cases, on_delete=models.CASCADE)

    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "     工程案例图集"

# 报价
class Price(models.Model):
    area = models.IntegerField("车间面积(m²)")
    level = models.IntegerField("净化级别")
    name = models.CharField("姓名", max_length=30)
    sex = models.SmallIntegerField("性别")
    mobile = models.IntegerField("手机号")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "      客户报价表"

    def colored_sex(self):
        if self.sex == 1:
            color_code = 'blue'
            sex = '男'
        else:
            color_code = 'red'
            sex = '女'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            sex,
        )

    colored_sex.short_description = '性别'

    level_dic =  {1:"三十万级净化工程",2:"十万级净化工程",3:"万级净化工程",4:"千级净化工程",5:"百级净化工程"}
    def show_level(self):
        return self.level_dic[self.level]

    show_level.short_description = '净化级别'



# bannner
# 首页轮播
class Banner(models.Model):
    OPEN_CHOICES = (
        ('_self', '当前窗口'),
        ('_blank', '新窗口'),
    )
    ORDER_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    )

    image = models.ImageField("图片", upload_to='banner/',help_text="建议图片大小：1920*680像素")
    url = models.CharField("图片链接地址", max_length=150)
    open = models.CharField("链接打开方式",max_length=20,choices=OPEN_CHOICES,default="当前窗口")
    order = models.SmallIntegerField("排序", choices=ORDER_CHOICES,default='0',help_text="数值越小排序越前")
    is_deleted = models.BooleanField("状态",default=True,help_text="勾选表示可用")

    class Meta:
        verbose_name_plural = "轮番图片"

    def show_img(self):
        if self.image:
            url = reverse('home')
            return mark_safe('<a href="%s/media/%s" target="_blank"><img src="%s/media/%s" width=100 /></a>' % (settings.DOMAIN_NAME,self.image,settings.DOMAIN_NAME,self.image))
        else:
            return '(no image)'

    show_img.short_description = '轮番图片'

# Head_img
class Head_img(models.Model):

<<<<<<< HEAD
=======

# Head_img
class Head_img(models.Model):

>>>>>>> ee3c4bdd9c2548690632f258e9198245469b4ce0
    image = models.ImageField("图片", upload_to='head_img/',help_text="建议图片大小：1920*300像素")

    class Meta:
        verbose_name_plural = "导航图片"

    def show_img(self):
        if self.image:
            url = reverse('home')
            return mark_safe('<a href="%s/media/%s" target="_blank"><img src="%s/media/%s" width=100 /></a>' % (settings.DOMAIN_NAME,self.image,settings.DOMAIN_NAME,self.image))
        else:
            return '(no image)'

    show_img.short_description = '导航图片'
<<<<<<< HEAD
=======

>>>>>>> ee3c4bdd9c2548690632f258e9198245469b4ce0
