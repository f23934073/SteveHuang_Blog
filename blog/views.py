from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Post ,Category,Tag,UpFile

from comments.forms import CommentForm
import markdown
from django import forms
import json

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk): 
    post = get_object_or_404(Post, pk=pk)
    post.increase_views() 
    form = CommentForm()
    comment_list = post.comment_set.all()#_set:針對一對多的查詢語法

    post.body = markdown.markdown(post.body,
                                  extensions=[ 'markdown.extensions.extra',
                                  'markdown.extensions.codehilite',
                                   'markdown.extensions.toc', ])
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }

    return render(request, 'blog/detail.html', context=context)

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month ).order_by('-created_time') 
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk): #記得在前面import Category
   cate = get_object_or_404(Category, pk=pk) 
   post_list = Post.objects.filter(category=cate).order_by('-created_time') 
   return render(request, 'blog/index.html', context={'post_list': post_list})

def TagView(request, pk): #記得在前面import Tag
   Tag_obj = get_object_or_404(Tag, pk=pk)
   post_list = Post.objects.filter(tags=Tag_obj).order_by('-created_time') 
   return render(request, 'blog/index.html', context={'post_list': post_list})


class UpFiles(forms.Form):
    upfile = forms.FileField()
    
def Editor(request):
    return render(request, 'blog/Editor.html')

def upload(request):
    if request.method == "POST":
        up = UpFiles(request.POST, request.FILES)
        cc = UpFile(up_file=request.FILES['file'])
        cc.save()
        url = 'http://127.0.0.1/' + str(cc.up_file)
        resp = {'success':1,'message': "6666",'url': url}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        print("NO")
        resp = {'success': 0, 'message': "error meth"}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    return render(request, 'blog/Editor.html')