from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Tag
from django.db.models import Q

#добавить теги 


def post_list(request):
    search_query = request.GET.get('search','')
    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query)
            |
            Q(body__icontains=search_query)
        )
    else:
        posts = Post.objects.all()
    return render(request,'blog/index.html',context={'posts': posts})



def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags.html', context={'tags':tags})


def post_detail(request,slug):
    post = Post.objects.get(slug = slug)
    return render(request,'blog/post_detail.html',context={'post': post})


def tag_detail(request,pk):
    tag = Tag.objects.get(pk=pk)
    return render(request,'blog/tag_detail.html',context={'tag': tag})

