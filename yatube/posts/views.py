from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    latest_posts = Post.objects.order_by("-pub_date")[:10]
    return render(request, "index.html", {"posts": latest_posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    posts = Post.objects.filter(group=group).order_by("-pub_date")[:10]
    context = {'group': group, 'posts': posts}
    return render(request, "group.html", context)
