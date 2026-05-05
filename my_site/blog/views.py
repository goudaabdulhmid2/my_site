from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic import View

from .models import Post, Comment
from .forms import CommentForm

class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ["-date"]
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
  

class PostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

class PostView(View):

    def is_saved_for_later(self, request, post_id):
        stored_posts = request.session.get("stored_posts", [])
        return post_id in stored_posts


    def get(self, request, slug):
        post = get_object_or_404(
            Post.objects.prefetch_related("tags", "comments"),
            slug=slug
        )

        comment_form = CommentForm()
        comments = post.comments.all().order_by("-date")
        count = post.comments.count()
        
        stored_posts = request.session.get("stored_posts", [])
        is_saved_for_later = post.id in stored_posts

        return render(request, "blog/post-details.html", {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": comments,
            "count": count,
            "is_saved_for_later": self.is_saved_for_later(request, post.id)
        })
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)

        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        

        comments = post.comments.all().order_by("-date")
        count = post.comments.count()
        
        stored_posts = request.session.get("stored_posts", [])
        is_saved_for_later = post.id in stored_posts

        return render(request, "blog/post-details.html", {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": comments,
            "count": count,
            "is_saved_for_later": self.is_saved_for_later(request, post.id)
        })
   

class ReadLaterView(View):
    def post(self, request):
        stored_posts = request.session.get("stored_posts", [])
        
        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
            
        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
    def get(self, request):
        stored_posts = request.session.get("stored_posts", [])
        
        posts = Post.objects.filter(id__in=stored_posts)

        return render(request, "blog/stored-posts.html", {
            "posts": posts,
            "has_posts": len(posts) > 0
        })