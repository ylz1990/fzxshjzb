# coding=utf8
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import Article,College
from datetime import datetime




# 首页
def xsj_index(request):
    context = {}
    # blog_list = Article.objects.all().order_by("-pub_time")
    blog_list = Article.objects.filter(new_type__contains='公司新闻').order_by("-pub_time")
    blog_list1 = Article.objects.filter(new_type__contains='行业新闻').order_by("-pub_time")

    context['blog_list'] = blog_list
    context['blog_list1'] = blog_list1
    return render(request,"xsjzb/index.html",context)


# 成功案例
def xsj_cgal(request):
    return render(request,"xsjzb/chenggonganli.html")


# 关于华企
def xsj_gyhq(request):
    return render(request,"xsjzb/guanyuhuaqi.html")

def xsj_about_1(request):
    return render(request,"xsjzb/about_1.html")

def xsj_about_2(request):
    return render(request,"xsjzb/about_2.html")

# 联系我们
def xsj_lxwm(request):
    return render(request,"xsjzb/lianxiwomen.html")

# 留言板
def xsj_lyb(request):
    return render(request, "xsjzb/liuyanban.html")

# 个人主页
def xsj_per(request):
    return render(request, "xsjzb/personal.html")

# 新闻中心   每页显示10条数据
def xsj_xwzx(request):
    context = {}
    blog_list = Article.objects.all().order_by("-pub_time")
    page_robot = Paginator(blog_list,10)
    try:
        blog_list = page_robot.page(request.GET.get("page"))
    except PageNotAnInteger:
        blog_list = page_robot.page(1)
    except EmptyPage:
        blog_list = page_robot.page(page_robot.num_pages)
    context['blog_list'] = blog_list
    return render(request, "xsjzb/xinwenzhongxin.html",context)

# 公司新闻中心   每页显示10条数据
def xsj_gsxw(request):
    context = {}
    blog_list = Article.objects.filter(new_type__contains='公司新闻').order_by("-pub_time")
    page_robot = Paginator(blog_list,10)
    try:
        blog_list = page_robot.page(request.GET.get("page"))
    except PageNotAnInteger:
        blog_list = page_robot.page(1)
    except EmptyPage:
        blog_list = page_robot.page(page_robot.num_pages)
    context['blog_list'] = blog_list
    return render(request, "xsjzb/companynew.html",context)

# 行业新闻中心   每页显示10条数据
def xsj_hyxw(request):
    context = {}
    blog_list = Article.objects.filter(new_type__contains='行业新闻').order_by("-pub_time")
    page_robot = Paginator(blog_list,10)
    try:
        blog_list = page_robot.page(request.GET.get("page"))
    except PageNotAnInteger:
        blog_list = page_robot.page(1)
    except EmptyPage:
        blog_list = page_robot.page(page_robot.num_pages)
    context['blog_list'] = blog_list
    return render(request, "xsjzb/hangyexinwen.html",context)
# 新闻中心详情
def xsj_xqy(request,blog_id):
    blog = Article.objects.get(id=blog_id)
    return render(request, "xsjzb/xinwenzhongxin_xqy.html",context={"blog":blog})

# 业务介绍
def xsj_ywjs(request):
    context = {}
    gold1 = College.objects.get(id=1)
    gold2 = College.objects.get(id=2)
    gold3 = College.objects.get(id=3)
    gold4 = College.objects.get(id=4)
    gold5 = College.objects.get(id=5)
    gold6 = College.objects.get(id=6)
    context['gold1'] = gold1
    context['gold2'] = gold2
    context['gold3'] = gold3
    context['gold4'] = gold4
    context['gold5'] = gold5
    context['gold6'] = gold6
    return render(request, "xsjzb/yewujieshao.html", context)

# 业务中心详情
def xsj_col(request, blog_id):
    context = {}
    blog = College.objects.get(id=blog_id)
    gold1 = College.objects.get(id=1)
    gold2 = College.objects.get(id=2)
    gold3 = College.objects.get(id=3)
    gold4 = College.objects.get(id=4)
    gold5 = College.objects.get(id=5)
    gold6 = College.objects.get(id=6)
    context['gold1'] = gold1
    context['gold2'] = gold2
    context['gold3'] = gold3
    context['gold4'] = gold4
    context['gold5'] = gold5
    context['gold6'] = gold6
    context['blog'] = blog
    return render(request, "xsjzb/yewujieshao_xqy.html", context)

# 添加文章
# def xsj_add(request):
#     return render(request, "xsjzb/add.html")
# # 添加文章
# def xsj_add_handle(request):
#     title = request.POST.get('title')
#     author = request.POST.get('author')
#     content = request.POST.get('content')
#     pub_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     new_type = request.POST.get("new")
#     blog = Article(title=title, author=author,pub_time=pub_time,content=content,new_type=new_type)
#     blog.save()
#     return render(request, "xsjzb/add.html")
#
# # 编辑文章的页面
# def xsj_edit(request):
#     context = {}
#     blog_list = Article.objects.all().order_by("-pub_time")
#     page_robot = Paginator(blog_list, 10)
#     try:
#         blog_list = page_robot.page(request.GET.get("page"))
#     except PageNotAnInteger:
#         blog_list = page_robot.page(1)
#     except EmptyPage:
#         blog_list = page_robot.page(page_robot.num_pages)
#     context['blog_list'] = blog_list
#     return render(request,"xsjzb/edit.html", context)
#
# # 删除文章
# def delete(request, blog_id):
#     blog = Article.objects.get(id=blog_id)
#     if blog:
#         blog.delete()
#         return redirect(reverse('edit'))
#     else:
#         return HttpResponse("没有这篇博客")
#
# # 修改文章
# def alter(request, blog_id):
#     blog = Article.objects.get(id=blog_id)
#     if request.method == "GET":
#         return render(request,'xsjzb/alter.html',context={"blog":blog})
#     elif request.method == "POST":
#         title = request.POST.get("title")
#         author = request.POST.get("author")
#         content = request.POST.get("content")
#         blog.title = title
#         blog.author = author
#         blog.content = content
#         blog.save()
#         return redirect(reverse("edit"))

# def college(request):




