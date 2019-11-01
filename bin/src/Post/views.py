from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post
from .forms import PostForm


def getAll(request):
    # all_posts = Post.objects.all()
    all_posts = Post.objects.filter(active=True)
    context = {'all_posts': all_posts}
    return render(request, 'all_posts.html', context)


def getById(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)

    context = {'post': post}
    return render(request, 'info.html', context);
    # return HttpResponse("Hello, world. You're at the polls index.")


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
    else:
        form = PostForm()
    # return HttpResponse(request.GET.get("q", None));

    context = {'form': form}

    return render(request, 'create.html', context)


def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
    else:
        form = PostForm(instance=post)
    # return HttpResponse(request.GET.get("q", None));

    context = {'form': form}

    return render(request, 'edit.html', context)
