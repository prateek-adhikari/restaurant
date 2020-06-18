from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from blog.models import Post,Category, Comment
from taggit.models import Tag
from blog.forms import CommentForm
# Create your views here.
def post_list(request):
    post_list = Post.objects.all()

    search_query = request.GET.get('q')
    if search_query:
        post_list = post_list.filter(
            Q(title__icontains = search_query)|
            Q(content__icontains = search_query)
        )

    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 3)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context = {
        "post": post_list
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

