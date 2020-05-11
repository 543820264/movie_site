from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, Page


# Create your views here.
def index(request):
    # list_2 = List_1.objects.all().values('id', 'name', 'list_2__id', 'list_2__name')

    return render(request, 'index.html')





def list(request, cname):
    # 当前列表
    # 当前电影列表
    movies_obj = Movies.objects.filter(column__url=cname)
    current_list = movies_obj.all().values('column_id', 'column__name', 'column__url', 'column__parent__name').first()
    current_list_cname = current_list['column__url']

    print(current_list['column__url'])
    movies_list = []
    # 分页
    for i in movies_obj:
        movies_list.append(i)
    paginator = Paginator(movies_list, 10)

    posts = paginator.page(1)

    context = {'current_list': current_list,
               'movies_list': movies_list,
               'posts': posts,
               'current_list_cname': current_list_cname
               }

    return render(request, 'list.html', context)

def list_page(request, cname,  current_page):
    # 当前列表
    # 当前电影列表
    movies_obj = Movies.objects.filter(column__url=cname)
    current_list = movies_obj.all().values('column_id', 'column__name', 'column__url', 'column__parent__name').first()
    current_list_cname = current_list['column__url']

    print(current_list['column__url'])
    movies_list = []
    # 分页
    for i in movies_obj:
        movies_list.append(i)
    paginator = Paginator(movies_list, 10)
    if current_page == "":
        current_page = 1
    else:
        current_page = current_page
    posts = paginator.page(current_page)

    context = {'current_list': current_list,
               'movies_list': movies_list,
               'posts': posts,
               'current_list_cname': current_list_cname
               }

    return render(request, 'list.html', context)

def movies_content(request, mid):
    movies_obj = Movies.objects.get(id=mid)
    context = {'movies_obj': movies_obj}
    return render(request, 'content.html', context)


def movies_play(request, mid):
    movies_obj = Movies.objects.get(id=mid)
    context = {'movies_obj': movies_obj}
    return render(request, 'play.html', context)


