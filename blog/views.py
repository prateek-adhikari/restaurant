from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post,Category, Comment
from taggit.models import Tag
from blog.forms import CommentForm
# Create your views here.
def post_list(request):
    post = Post.objects.all()
    paginator = Paginator(post, 1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        "post": post,
    }
    return render(request, 'blog/blog.html', context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    categories = Category.objects.all()
    all_tags = Tag.objects.all()
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm()
    if request.method=="POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
    context = {
        "post": post,
        "categories": categories,
        "all_tags": all_tags,
        "comments": comments,
        "comment_form": comment_form
    }
    return render(request, 'blog/blog-single.html', context)

def post_by_tag(request, tag):
    post = Post.objects.filter(tags__name__in=[tag])
    context = {
        "post": post
    }
    return render(request, 'blog/blog.html', context)


def post_by_category(request, category):
    post = Post.objects.filter(category__category_name=category)
    context = {
        "post": post
    }
    return render(request, 'blog/blog.html', context)

