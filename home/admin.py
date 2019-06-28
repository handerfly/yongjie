from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'update_time')

@admin.register(Honer)
class HonerAdmin(admin.ModelAdmin):
    list_display = ('title', 'images', 'update_time')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('content', 'update_time')

@admin.register(NewsType)
class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_time')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'author','show_content', 'viewed','update_time')

    # list_editable 设置默认可编辑字段（category默认不可编辑，因为它是一个链接，点击会进入修改页面）
    list_editable = ['type', ]

    # fk_fields 设置显示外键字段
    fk_fields = ('type',)

    # 过滤器功能及能过滤的字段
    list_filter = ('type', 'author', 'update_time')
    # 搜索功能及能实现搜索的字段
    search_fields = ('title', 'type', 'author','show_content', 'viewed','update_time')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',"title",)

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id','category','title', 'order','update_time')

    # list_editable 设置默认可编辑字段（category默认不可编辑，因为它是一个链接，点击会进入修改页面）
    list_editable = ['category','order', ]

    # fk_fields 设置显示外键字段
    fk_fields = ('category',)

    # 过滤器功能及能过滤的字段
    list_filter = ('category', 'update_time')
    # 搜索功能及能实现搜索的字段
    search_fields = ('category','title', 'order','update_time')

class ProductImgsInline(admin.TabularInline):
    model = ProductImgs
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImgsInline]
    list_display = ('title', 'category','type','sub_type', 'show_detail', 'update_time')

    # list_editable 设置默认可编辑字段（category默认不可编辑，因为它是一个链接，点击会进入修改页面）
    list_editable = ['category', 'type']

    # fk_fields 设置显示外键字段
    fk_fields = ('category','type')

    # 过滤器功能及能过滤的字段
    list_filter = ('category','type','sub_type')
    # 搜索功能及能实现搜索的字段
    search_fields = ('title', 'category','type','sub_type', 'show_detail')

@admin.register(ProductImgs)
class ProductImgsAdmin(admin.ModelAdmin):
    list_display = ('images', 'product', 'update_time')

@admin.register(SolutionType)
class SolutionTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'order','update_time')
    list_editable = ['order', ]


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'type', 'cover','show_detail', 'update_time')
    list_editable = ['order', 'type']

    # fk_fields 设置显示外键字段
    fk_fields = ('type',)

    # 过滤器功能及能过滤的字段
    list_filter = ('type', )
    # 搜索功能及能实现搜索的字段
    search_fields = ('title', 'type', 'show_detail')

class CasesImgsInline(admin.TabularInline):
    model = CasesImgs
    extra = 1

@admin.register(Cases)
class CasesAdmin(admin.ModelAdmin):
    inlines = [CasesImgsInline]
    list_display = ('title', 'solution','type', 'detail', 'update_time')
    list_editable = ['type','solution']

    # fk_fields 设置显示外键字段
    fk_fields = ('type',)

    # 过滤器功能及能过滤的字段
    list_filter = ('type','solution')
    # 搜索功能及能实现搜索的字段
    search_fields = ('title', 'solution','type', 'detail','update_time')

@admin.register(CasesImgs)
class CasesImgsAdmin(admin.ModelAdmin):
    list_display = ('images', 'cases', 'update_time')

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('area','show_level','name','colored_sex','mobile')
    # 过滤器功能及能过滤的字段
    list_filter = ('area', 'show_level','colored_sex')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'show_img', 'url', 'open', 'order','is_deleted')
    list_filter = ('is_deleted',)
    list_editable = ['order', ]
    # 过滤器功能及能过滤的字段
    list_filter = ('is_deleted', )

admin.site.site_header = '广州顺尚净化网后台管理'
admin.site.site_title = '广州顺尚净化网'


