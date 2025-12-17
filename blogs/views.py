from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """首页：按时间倒序展示所有博文"""
    # 阶段2要求：所有人（含游客）可见
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_blog(request):
    """添加新博文"""
    # 阶段2要求：仅登录用户可访问
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = BlogPostForm()
    else:
        # POST提交的数据：对数据进行处理
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            # 阶段2关键点：将新博文关联到当前登录用户
            new_post.author = request.user
            new_post.save()
            return redirect('blogs:index')

    context = {'form': form, 'title': '发布新博文'}
    return render(request, 'blogs/post_form.html', context)

@login_required
def edit_blog(request, blog_id):
    """编辑既有博文"""
    post = get_object_or_404(BlogPost, id=blog_id)

    # 阶段2关键点：权限校验
    # 只有作者本人可以编辑，否则返回403禁止访问
    if post.author != request.user:
        return HttpResponseForbidden("您没有权限编辑这篇博文。")

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = BlogPostForm(instance=post)
    else:
        # POST提交的数据，对数据进行处理
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'form': form, 'post': post, 'title': f'编辑：{post.title}'}
    return render(request, 'blogs/post_form.html', context)