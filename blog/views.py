from django.shortcuts import render
from blog.models import Post,Category
# Create your views here.
def post_list(request):
    post = Post.objects.all()
    context = {
        "post": post
    }
    return render(request, 'blog/blog.html', context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post
    }
    return render(request, 'blog/blog-single.html', context)
