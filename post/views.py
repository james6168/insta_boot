from django.shortcuts import render
from post.models import Post

# Create your views here.


def get_all_posts(request):
    posts = Post.objects.all()
    return render(request, "post/posts.html", locals())