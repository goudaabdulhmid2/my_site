from django.shortcuts import render, get_object_or_404
import json
from pathlib import Path

from .models import Post

# Create your views here
# read data from json
def get_all_posts():
    posts_file = Path(__file__).resolve().parent.parent / "dummy_posts.json"
    try:
        with posts_file.open("r", encoding="utf-8") as file:
            data = file.read()
            return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def get_date(post):
    return post["date"]

def starting_page(request):
    least_three_posts = Post.objects.all().order_by("-date")[:3]
    
    return render(request, 'blog/index.html', context={
        "posts": least_three_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, 'blog/all-posts.html', context={
        "posts": all_posts
    })


def post_detail(request, slug):
    post = get_object_or_404(Post,slug=slug)

    return render(request,"blog/post-details.html", context={
        "post":post,
        "post_tags":post.tags.all()
    })