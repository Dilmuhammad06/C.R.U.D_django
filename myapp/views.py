from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm
from .forms import UpdateForm

def index(request):
    post = Post.objects.all()
    data = {
        'posts':post
    }
    return render(request,'index.html',data)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request,'create.html',{'form':form})

def delete(request,post_slug):
    pr = Post.objects.get(slug=post_slug)
    pr.delete()
    return redirect('home')

def update_post(request, edit_slug):
    post = get_object_or_404(Post, slug=edit_slug)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = UpdateForm(instance=post)
    return render(request, 'edit.html', {'form': form})