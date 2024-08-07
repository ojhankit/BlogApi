from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Blog ,CustomUser ,Comment
from .forms import BlogForm ,CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request ,'blog/blog_list.html' ,{'blogs':blogs})

@login_required
def blog_list_user(request ,pk):
    user = get_object_or_404(CustomUser ,pk = pk)
    user_blog = Blog.objects.filter(user = user)
    return render(request ,'blog/user_blog.html' ,{'user_blog':user_blog ,'user':user})

@login_required
def blog_detail(request ,blog_id):
    blog = get_object_or_404(Blog ,id=blog_id)
    comments = Comment.objects.filter(blog=blog)
    return render(request ,'blog/blog_detail.html' ,{'blog':blog ,'comments':comments})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blog_list')  # Adjust this to your actual blog list view name
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})

@login_required
def delete_blog(request ,pk):
    blog = get_object_or_404(Blog ,pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('user_blog')
    else:
        return render(request ,'blog/delete_confirm.html' ,{'blog':blog})
    
@login_required
def add_comment(request ,blog_id):
    blog = get_object_or_404(Blog ,id=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return redirect('blog_detail' ,blog_id=blog_id)
    else:
        form = CommentForm()
    return render(request ,'blog/add_comment.html' ,{'form':form ,'blog':blog})
    
