from django.shortcuts import redirect

from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.http import HttpResponse
from .models import Product
from django.shortcuts import render, get_object_or_404
from .forms import PostForm



def post_edit(request, pk):
    post = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_list(request):
    posts = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'home.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Product, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect(post_list)
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/registration.html', context)
# Create your views here.
