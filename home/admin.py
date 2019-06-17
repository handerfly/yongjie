from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'update_time')

@admin.register(Honer)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'images', 'update_time')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('content', 'update_time')

@admin.register(NewsType)
class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_time')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'author','content', 'viewed','update_time')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',"title",)

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('category','title', 'order','update_time')

class ProductImgsInline(admin.TabularInline):
    model = ProductImgs
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImgsInline]
    list_display = ('title', 'category','type','sub_type', 'detail', 'update_time')

@admin.register(ProductImgs)
class ProductImgsAdmin(admin.ModelAdmin):
    list_display = ('images', 'product', 'update_time')

@admin.register(SolutionType)
class SolutionTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_time')

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'cover','detail', 'update_time')

class CasesImgsInline(admin.TabularInline):
    model = CasesImgs
    extra = 1

@admin.register(Cases)
class CasesAdmin(admin.ModelAdmin):
    inlines = [CasesImgsInline]
    list_display = ('title', 'solution','type', 'detail', 'update_time')

@admin.register(CasesImgs)
class CasesImgsAdmin(admin.ModelAdmin):
    list_display = ('images', 'cases', 'update_time')

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('area','show_level','name','colored_sex','mobile')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'show_img', 'url', 'open', 'order','is_deleted')
    list_filter = ('is_deleted',)


admin.site.site_header = '广州顺尚净化网后台管理'
admin.site.site_title = '广州顺尚净化网'


