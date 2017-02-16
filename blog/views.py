from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Comment, Tag
from blog.forms import PostForm
def post_list(request):
    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', { 'posts' : posts,})

def blog_new(request):
    if request.method == 'GET':
        form = PostForm()
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print('통과한 값 : ', form.cleaned_data)
            # return redirect(post)
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog:post_list')
    return render(request, 'blog/post_form.html', {
        'form': form,
    })

def post_detail(request, id): #pk로도 id에 접근가능, str임
    post = Post.objects.get(id=id)
    comment = Comment.objects.filter(post=id)
    tag = Tag.objects.filter(post=id)
    return render(request, 'blog/post_detail.html',{'post':post, 'comment':comment,'tag':tag})