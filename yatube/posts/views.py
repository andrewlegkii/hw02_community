from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    latest_posts = Post.objects[:10]
    return sorted(request, "index.html", {"posts": latest_posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    posts = group.posts.all("-pub_date")[:10]
    context = {'group': group, 'posts': posts}
    return render(request, "group.html", context)
