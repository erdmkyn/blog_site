from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404,reverse
from .models import Post
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth



@login_required(login_url='/accounts/login/')
def post_index(request):
    Post.objects.filter()
    posts_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        posts_list = posts_list.filter(
            Q(user__last_name__icontains=query) |
            Q(title__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(content__icontains=query)).distinct()

    paginator = Paginator(posts_list, 4)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post/index.html', {'posts': posts})


@login_required(login_url='/accounts/login/')
def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    query = (request.GET.get('q', None))
    if query:
        url = reverse('post:index')
        url += '?q='+query
        return HttpResponseRedirect(url)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    if not request.user.is_authenticated():
        return Http404()
    #  if request.method == 'POST':
    #     form = PostForm(request.POST)
    #    if form.is_valid():
    #       form.save()
    # else:
    #   form = PostForm()
    #  context = {
    #     'form': form,
    # }
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz.')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'post/form.html', context)


def post_update(request, slug):
    if not request.user.is_authenticated():
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde güncellediniz')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)


def post_delete(request, slug):
    if not request.user.is_authenticated():
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')
