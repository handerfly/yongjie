from django.shortcuts import render, get_object_or_404
from home.models import *
from django.core.paginator import Paginator
from django.conf import settings
from yongjie.form import PriceForm
from django.http import HttpResponseRedirect,HttpResponse
import json

def get_list_common_data(request, all_list):
    paginator = Paginator(all_list, settings.EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get('page', 1) # 获取url的页面参数（GET请求）
    page_of_obj = paginator.get_page(page_num)
    currentr_page_num = page_of_obj.number # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))

    context = {}
    context['page_of_obj'] = page_of_obj
    context['page_range'] = page_range
    context['count'] = paginator.num_pages

    return context

# 首页
def index(request):
	context = {}
	# 轮番图片
	banners = Banner.objects.filter(is_deleted=True).order_by('order')

	# 解决方案
	solutions = Solution.objects.all()[:4]

	# 案例
	cases = Cases.objects.all()[:8]

	# 荣誉
	honer = Honer.objects.all()[:6]

	# 动态
	news_type = NewsType.objects.all()[:3]
	news_dic = {}
	for each_type in news_type:
		news_objs = News.objects.filter(type=each_type)[:6]
		each_type = str(each_type)
		news_dic[each_type] = news_objs

	context['banners'] = banners
	context['solutions'] = solutions
	context['cases'] = cases
	context['honer'] = honer
	context['news'] = news_dic
	return render(request, 'mobile/index.html', context)

# 案例
def cases(request, type):
	#  没有传
	if type == 0:
		all_cases = Cases.objects.all()
	else:
		type_obj = get_object_or_404(SolutionType, id=type)
		all_cases = Cases.objects.filter(solution=type_obj)

	# 所有分类
	cases_type_objs = SolutionType.objects.all()

	context = get_list_common_data(request, all_cases)
	context['cases_types'] = cases_type_objs
	context['type'] = type

	return render(request, 'mobile/cases.html', context)

# 案例详情
def case_detail(request, case_id):
	# get the case object
	case_obj = get_object_or_404(Cases, id=case_id)
	# get the images
	images = CasesImgs.objects.filter(cases=case_obj)

	context = {}
	context['case'] = case_obj
	context['images'] = images
	return render(request, 'mobile/case_detail.html', context)

# 产品
def products(request, type):
	#  没有传
	if type ==0:
		all_products = Product.objects.all()
	else:
		type_obj = get_object_or_404(ProductType, id=type)
		all_products = Product.objects.filter(type=type_obj)

	# 所有分类
	product_type_objs = ProductType.objects.all()

	context = get_list_common_data(request, all_products)
	context['product_types'] = product_type_objs
	context['type'] = type
	return render(request, 'mobile/products.html', context)

# 产品详情
def product_detail(request, product_id):
	# get the product object
	product_obj = get_object_or_404(Product, id=product_id)
	# get the images
	images = ProductImgs.objects.filter(product=product_obj)
	# get all product types
	product_type_objs = ProductType.objects.all()

	type_id = product_obj.type.id

	context = {}
	context['product'] = product_obj
	context['product_types'] = product_type_objs
	context['images'] = images
	context['type'] = type_id
	return render(request, 'mobile/product_detail.html', context)

# 解决方案
def solution(request):
	# 所有的解决方案
	solution_objs = Solution.objects.all()

	context = {}
	context['solutions'] = solution_objs
	return render(request, 'mobile/solution.html',context)

# 解决方案详情
def solution_detail(request, solution_id):
	solution_obj = get_object_or_404(Solution, id=solution_id)

	# 找出所有相关type的案例
	relate_cases = Cases.objects.filter(solution=solution_obj.type)[:10]

	# 更多案例
	more_solutions = Solution.objects.exclude(id=solution_obj.id)[:4]

	context = {}
	context['solution'] = solution_obj
	context['relate_cases'] = relate_cases
	context['more_solutions'] =more_solutions
	return render(request, 'mobile/solution_detail.html', context)


# 售后服务
def service(request):
	# 服务承诺
	service = Service.objects.filter().first()

	context = {}

	context['service'] = service

	return render(request, 'mobile/service.html',context)


# 新闻
def news(request, type):
	TYPE_DIC = {1: '顺尚动态', 2: '行业资讯', 3: '净化技术'}

	if not type in range(1,4):
		type = 0
		str_type = "全部新闻"
		news_objs = News.objects.all()
	else:
		newstype_obj = NewsType.objects.get(title=type)
		str_type = TYPE_DIC[newstype_obj.title]

		news_objs = News.objects.filter(type=newstype_obj)

	context = get_list_common_data(request, news_objs)

	return  render(request, 'mobile/news.html',context)

# 行业资讯详情
def news_detail(request, news_id):
	news = get_object_or_404(News, id=news_id)

	type_obj = news.type


	context = {}
	context['news'] = news
	# 上一篇 下一篇
	context['pre_news'] = News.objects.filter(update_time__gt=news.update_time,type=type_obj).first()
	context['next_news'] = News.objects.filter(update_time__lt=news.update_time,type=type_obj).last()
	context['type'] = str(news.type)
	news.viewed += 1
	news.save()
	return render(request, 'mobile/news_detail.html', context)

# 关于我们
def about(request, about_id):
	TYPE_DIC = {1:'公司简介', 2:'文化理念',3:'联系我们'}

	about = get_object_or_404(About, title=about_id)
	context = {}
	context['about'] = about
	context['title'] = TYPE_DIC[about.title]
	return render(request, 'mobile/about.html', context)

# 荣誉资质
def honer(request):
	honer = Honer.objects.all()
	context = {}
	context['honer'] = honer
	return render(request, 'mobile/honer.html', context)

def quote(request):
    return  render(request, 'mobile/quote.html')

# 实验环境系统
def price(request):

	if request.is_ajax():
		area   = request.POST.get("area")
		level  = request.POST.get("level")
		name   = request.POST.get("name")
		sex    = request.POST.get("sex")
		mobile = request.POST.get("mobile")
		price_obj = Price.objects.create(
			area=area,
			level=level,
			name=name,
			sex=sex,
			mobile=mobile,
		)
		if price_obj:
			return HttpResponse(json.dumps({'status':'success'}))
	else:
		return HttpResponse(json.dumps({'status':'fail','msg':"请您正确填写表单"}))



