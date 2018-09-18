from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('precio')
    return render(request, 'blog/post_list.html', {'posts': posts})

#def post_list(request):
#	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('precio')
#	return render(request, 'blog/post_list.html', {'posts':posts})

def post_list_mayor(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-precio')
    return render(request, 'blog/post_list_mayor.html', {'posts':posts})    

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('listado')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('listado')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_list_procesadores(request):
    posts = Post.objects.all().filter(componentes="Procesadores", published_date__lte=timezone.now()).order_by('precio')
    return render(request, 'blog/procesadores.html', {'posts': posts})

def post_list_procesadores_menor(request):
    posts = Post.objects.filter(componentes="Procesadores", published_date__lte=timezone.now()).order_by('-precio')
    return render(request, 'blog/procesadores_menor.html', {'posts':posts})

def post_list_placa_video(request):
    posts = Post.objects.all().filter(componentes="Placa Video", published_date__lte=timezone.now()).order_by('precio')
    return render(request, 'blog/placa_video.html', {'posts': posts})

def post_list_otros(request):
    posts = Post.objects.all().filter(componentes="Otros", published_date__lte=timezone.now()).order_by('precio')
    return render(request, 'blog/otros.html', {'posts': posts})

def post_list_placa_video_menor():
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-precio')
    return render(request, 'blog/placa_video_menor.html', {'posts': posts})

def post_list_otros_menor(request):
    posts = Post.objects.all().filter(componentes="Otros", published_date__lte=timezone.now()).order_by('-precio')
    return render(request, 'blog/otros_menor.html', {'posts': posts})