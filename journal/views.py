from django.shortcuts import render
from journal.models import Post
from journal.forms import PostForm
def post_list(request):
    posts = Post.objects.all()

    return render(request, 'journal/post_list.html', { 'posts' : posts,})

def post_new(request):
    form = PostForm()
    return render(request, 'journal/post_new.html',{'form':form})

def post_detail(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'journal/post_detail.html',{'post':post,})
