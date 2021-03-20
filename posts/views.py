from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post, Group


def index(request):
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    return render(request, "group.html", {"group": group, "posts": posts})


def new_post(request):
    form = PostForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('index')
    return render(request, 'new_post.html', {'form': form})
