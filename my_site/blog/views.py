from django.shortcuts import render
import json
from pathlib import Path

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
    all_posts = get_all_posts()
    sorted_posts = sorted(all_posts, key=get_date, reverse=True)
    least_three_posts = sorted_posts[:3]

    return render(request, 'blog/index.html', context={
        "posts": least_three_posts
    })


def posts(request):
    all_posts = get_all_posts()
    return render(request, 'blog/all-posts.html', context={
        "posts": all_posts
    })

def post_detail(request, slug):

    return render(request,"blog/post-details.html")