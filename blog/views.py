from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from .models import Post , Comment
from .forms import CommentForm
from .forms import PostForm  # فرض کنید یک فرم برای ویرایش پست دارید



def index(request):
    search_id = request.GET.get('search_id')  # دریافت شناسه از پارامترهای GET
    if search_id:
        # فیلتر کردن پیام‌ها بر اساس شناسه
        posts = Post.objects.filter(id=search_id)  # فیلتر بر اساس ID
    else:
        posts = Post.objects.all()  # اگر شناسه‌ای وجود نداشت، همه پیام‌ها را بگیر

    paginator = Paginator(posts, 2)  # صفحه‌بندی پیام‌ها
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'homeblog.html', {'page_obj': page_obj})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()  # بارگذاری کامنت‌ها

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # فرض بر این است که کاربر وارد شده است
            comment.save()
            return redirect('blog:post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # بررسی اینکه آیا کاربر مجاز به حذف است
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'پست با موفقیت حذف شد.')
        return redirect('blog:index')

    return render(request, 'homeblog.html', {'object': post})


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:index')  # به صفحه اصلی یا صفحه مورد نظر هدایت کنید
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})